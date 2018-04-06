from boolean3 import tokenizer
from ipdb import set_trace
from os.path import basename,dirname

tempcode="""
from numpy.random import random
import os, sys
import time
from ipdb import set_trace
from itertools import combinations, combinations_with_replacement
import hashlib
import json

__start_time = 0

FP_LENGTH = 10

def update(idx, max_idx, updates=1000, blocks=20):    
    global __start_time
    idx += 1
    if idx == 1:
        __start_time = time.time()
    elapsed_time = time.time() - __start_time
    avgtime = elapsed_time / idx;
    remaintime = (max_idx - idx)*avgtime
    if idx>max_idx:
        idx = max_idx
    # updates = 1000
    if max_idx < updates:
        updates = max_idx
    sys.stdout.flush()
    # blocks = 50
    if idx % (max_idx/updates) == 0 or (idx == max_idx):
        p = float(idx)/float(max_idx)
        s = '\\r[%s] %.02f%% (%.01fs)' % ('#'*int(p*blocks), p*100.0, remaintime)
        sys.stdout.write(s)
        sys.stdout.flush()

    if idx == max_idx:
        sys.stdout.write('\\n')
        sys.stdout.flush()

cdef detect_cycles( data ):
    fsize   = len(data)
    for msize in range(1, int(fsize/2) + 1):
        for index in range(fsize):
            left  = data[index:index+msize]
            right = data[index+msize:index+2*msize]
            if left == right:
                return index, msize

    return 0, 0

$MODELCODE$

def fp(s):
    res = hashlib.sha224(repr(s).encode('utf-8')).hexdigest()
    return res[0:FP_LENGTH]

def prettify(state_data, trajectory=False):
    if trajectory==False: 
        return "".join( ['%d'%s for s in state_data] )        
    else:
        traj_value = [] 
        for state in state_data: 
            state_str = []
            for st0 in state:
                state_str.append('%d' % st0)

            traj_value.append("".join(state_str))

        return "-".join(traj_value)

def main(steps=30, samples=100, debug=False, progress=False, on_states=[], off_states=[]):

    res = {} 
    seen = {} 
    traj = {}
    
    for i in range(samples):
        if progress: 
            update(i, samples)

        values = simulate(steps=steps, on_states=on_states, off_states=off_states)
        idx, size = detect_cycles(values)

        if size == 1:
            attr_type = 'point'
        elif size > 1:
            attr_type = 'cyclic'
        elif size == 0:
            attr_type = 'unknown'
        else:        
            assert False        

        if attr_type == 'cyclic':
            cyc = values[idx : idx + size]
            head = sorted(cyc)[0]
            left = cyc[cyc.index(head) : len(cyc)]
            right = cyc[0 : cyc.index(head)]
            raw_attr = left + right 
            attr_id = fp(raw_attr)
            attr = [] 
        
            for state in raw_attr:
                fp_value = fp(state)
                attr.append(fp_value)
                seen[fp_value] = prettify(state, trajectory=False)
        else: # point
            raw_attr = values[-1]
            attr_id = fp(raw_attr)
            attr = attr_id
            seen[attr_id] = prettify(raw_attr, trajectory=False)
        
        if attr_id in res: 
            res[attr_id]['count'] += 1
        else: 
            res[attr_id] = {} 
            res[attr_id]['count'] = 1 
            res[attr_id]['type'] = attr_type
            res[attr_id]['value'] = attr
    
        res[attr_id]['ratio'] = float(res[attr_id]['count']) / float(samples)

        if debug: 
            if attr_type=='cyclic':
                has_trajectory=True
            else: 
                has_trajectory=False

            traj[i] = {
                'value': prettify(values, trajectory=True),
                'type': attr_type, 
                'attr': prettify(raw_attr, trajectory=has_trajectory)
                }

    result = {
        'attractors': res, 
        'state_key': seen, 
        'trajectory': traj, 
        'labels': $LABELS$
        }

    return result
"""

def gencode(text):

    lexer = tokenizer.Lexer() 
    tokens = lexer.tokenize_text( text )
    node_list = sorted(list( tokenizer.get_nodes(tokens) ))

    init_tokens = tokenizer.init_tokens(tokens)
    update_tokens = tokenizer.update_tokens(tokens)

    ic_nodes = [] 
    for it in init_tokens:
        ic_nodes.append( it[0].value )

    update_nodes = [] 
    for it in update_tokens:
        update_nodes.append( it[0].value )        

    output_str = ''
    output_str += 'DEF num_nodes = %d\n' % len(node_list)
    output_str += 'ctypedef int (*cfptr)(int*)\n' 
    output_str += 'cdef cfptr eqlist[num_nodes]\n\n'

    remainer_node_ids = [i for i in range(0, len(node_list))]

    for it in update_tokens: 
        strout = '' 
        idx = node_list.index( it[0].value ) 
        remainer_node_ids.remove(idx)
        for i,el in enumerate(it): 
            if el.type=='ID':
                if i==0:
                    strout += 'state_%d'%node_list.index( el.value ) 
                else: 
                    strout += 'state[%d]'%node_list.index( el.value ) 
            elif el.type=='STATE': 
                if el.value=='Random':
                    strout += 'random()>0.5'
                else: 
                    strout += el.value
            elif el.type == 'AND' or el.type == 'OR' or el.type == 'NOT':
                strout += ' '+el.value+' '
            elif el.type == 'ASSIGN':
                continue
            else: 
                strout += el.value
        
        output_str += 'cdef int __bool_fcn_%d(int state[]):\n' % idx
        output_str += '    %s\n' % strout
        output_str += '    return state_%d\n\n' % idx

    for idx in remainer_node_ids:
        output_str += 'cdef int __bool_fcn_%d(int state[]):\n' % idx
        output_str += '    state_%d = state[%d]\n' % (idx, idx)
        output_str += '    return state_%d\n\n' % idx

    # output_str += 'cdef int __fixed_on(int state[]):\n'
    # output_str += '    return True\n\n'
    # output_str += 'cdef int __fixed_off(int state[]):\n'
    # output_str += '    return False\n\n'

    # for i in range(len(node_list)): 
    #     if node_list[i] in on_states:
    #         output_str+= 'eqlist[%d] = &__fixed_on\n' % (i) 
    #     elif node_list[i] in off_states: 
    #         output_str+= 'eqlist[%d] = &__fixed_off\n' % (i) 
    #     else: 
    #         output_str+= 'eqlist[%d] = &__bool_fcn_%d\n' % (i,i)    
    for i in range(len(node_list)): 
        output_str+= 'eqlist[%d] = &__bool_fcn_%d\n' % (i,i)            

    output_str+='\ncdef int state0[num_nodes]\n'
    output_str+='cdef int state1[num_nodes]\n\n'

    output_str+='def simulate(steps=10, on_states=[], off_states=[]):\n'
    output_str+='    node_list = %s\n' % repr(node_list)

    # initial_values 
    for it in init_tokens: 
        strout = '' 
        idx = node_list.index( it[0].value ) 
        for el in it: 
            if el.type=='ID':
                strout += 'state0[%d]'%node_list.index( el.value ) 
            elif el.type=='STATE': 
                if el.value=='Random':
                    strout += 'random()>0.5'
                else: 
                    strout += el.value
            else: 
                strout += el.value

        output_str+= '    ' + strout + '\n'

    # Previous version is 3sec. 
    output_str+= '    on_idxes = [ node_list.index(s) for s in on_states]\n'
    output_str+= '    off_idxes = [ node_list.index(s) for s in off_states]\n'

    output_str+= '    state_list = []\n'
    output_str+= '    state_list.append(state0)\n\n'
    output_str+= '    for i in range(steps):\n'
    output_str+= '        for k in range(num_nodes):\n'
    output_str+= '            state1[k] = eqlist[k](state0)\n'
    output_str+= '        for k in on_idxes:\n'
    output_str+= '            state1[k] = True\n'
    output_str+= '        for k in off_idxes:\n'    
    output_str+= '            state1[k] = False\n'
    output_str+= '        for k in range(num_nodes):\n'
    output_str+= '            state0[k] = state1[k]\n'
    output_str+= '        state_list.append(state0)\n\n'
    output_str+= '    return state_list\n'
    
    return output_str, node_list

def build(text):
    modelcode, node_list = gencode(text)
    result = tempcode.replace('$MODELCODE$', modelcode)
    result = result.replace('$LABELS$', repr(node_list))
    with open('engine.pyx', 'w') as f:
        f.write(result)
    
    # import pyximport; pyximport.install()

def run(samples=10, steps=10, debug=True, progress=False, on_states=[], off_states=[]): 
    
    import engine
    
    result = engine.main(samples=samples, steps=steps, debug=debug, \
        progress=progress, on_states=on_states, off_states=off_states)

    result['parameters'] = {
        'samples': samples,
        'steps': steps
        }

    return result
