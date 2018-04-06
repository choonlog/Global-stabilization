# -*- coding: utf-8 -*-
#!/usr/bin/python
#*************************************************************************
# Author: {Je-Hoon Song, <song.je-hoon@kaist.ac.kr>
#
# This file is part of {boolean3}.
#*************************************************************************

import os, sys
import time
from pdb import set_trace
from itertools import combinations, combinations_with_replacement

__start_time = 0

def update(idx, max_idx, updates=1000, blocks=20):
    """ This function is used for display progress bar in console environment.

    This function can be used to display the progression of the for-loops. In
    that case, the function should be called inside the loop, and total number
    of iteration(max_idx) and current index(idx) of the loop should be given to
    the function.

    For example:

        for i in range(0,100):
            update_progress(i, 100)

    This function can also be used to display the progress of normal function
    consists of several steps.

    For example:

        def my_function_with_3steps():

            update_progress(0, 3+1)

            ... step 1 ...
            update_progress(1, 3+1)

            ... step 2 ...
            update_progress(2, 3+1)

            ... step 3 ...
            update_progress(3, 3+1)


    Args:
        idx: current index of the for-loop
        max_idx: total number of iterations

    """
    global __start_time

    import sys

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
        s = '\r[%s] %.02f%% (%.01fs)' % ('#'*int(p*blocks), p*100.0, remaintime)
        sys.stdout.write(s)
        sys.stdout.flush()

    if idx == max_idx:
        sys.stdout.write('\n')
        sys.stdout.flush()
