'''
Created on Oct 27, 2013

@author: sina
'''

import requests
import requests_cache
from bs4 import BeautifulSoup
import logging

from utils.utils import setup_logger

class Level(object):
    '''
    Abstract class to solve puzzles on pythonchallenge.com 
    '''
    def __init__(self, url=None):
        self.soup = None
        self.url = url
        
        self.logger = setup_logger()
        self.logger.info('Solving %s located at %s' % (self.__class__.__name__.lower(), url))
        
        requests_cache.install_cache('/tmp/%s' % self.__class__.__name__)
        self.soup = BeautifulSoup(requests.get(self.url).content)


    def solve(self):
        NotImplementedError('This method must be implemented')
        
