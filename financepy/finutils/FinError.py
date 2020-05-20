# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 20:49:10 2016

@author: Dominic O'Kane
"""
###############################################################################
# Suppress error traceback messages in Jupyter

import traceback
import sys
from IPython import get_ipython

ipython = get_ipython()


def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
                   exception_only=False, running_compiled_code=False):
    etype, value, tb = sys.exc_info()
    return ipython._showtraceback(etype, value,
                                  ipython.InteractiveTB.get_exception_only(
                                      etype, value))

# sys.tracebacklimit = 0er
#ipython.showtraceback = hide_traceback

###############################################################################


def func_name():
    return traceback.extract_stack(None, 2)[0][2]


def isNotEqual(x, y, tol=1e-6):
    if abs(x - y) > tol:
        return True
    return False

###############################################################################


class FinError(Exception):
    ''' Simple error class specific to FinPy. Need to decide how to handle
    FinancePy errors. Work in progress. '''

    def __init__(self, message):
        ''' Create FinError object by passing a message string. '''
        self._message = message

    def print(self):
        print("FinError:", self._message)

###############################################################################
