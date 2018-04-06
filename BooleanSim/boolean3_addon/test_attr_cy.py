import json
from os.path import exists
from boolean3_addon import attr_cy

def test_this_1():

    modeltext = '''
    A= Random
    B= Random
    C= Random
    A*= A or C
    B*= A and C
    C*= not A or B
    '''
    # if not exists('engine.pyx'):
    attr_cy.build(modeltext)

    import pyximport; pyximport.install()

    res = attr_cy.run(samples=1000000, steps=50, debug=False, on_states=['A'], \
        progress=True)

    json.dump(res, open('test_attr_cy.json', 'w'), indent=4)

