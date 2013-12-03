'''
Created on Oct 27, 2013

@author: sina
'''

import logging

def setup_logger(verbose=False):
    if verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    return logging
