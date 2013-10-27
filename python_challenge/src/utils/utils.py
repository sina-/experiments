'''
Created on Oct 27, 2013

@author: sina
'''

import logging

def setup_logger():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    return logging
    