# -*- coding: utf-8 -*-
#!/usr/bin/python
#*************************************************************************
# Author: {Je-Hoon Song, <song.je-hoon@kaist.ac.kr>
#
# This file is part of {boolean3}.
#*************************************************************************

from boolean3_addon import progressbar

def test_update():

    import time

    for i in range(0,5):
        progressbar.update(i,5)
        time.sleep(1)
