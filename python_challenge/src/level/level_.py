'''
Created on Oct 27, 2013

@author: sina
'''

import requests
import requests_cache
from bs4 import BeautifulSoup
import logging

class Level(object):
    '''
    Abstract class to solve puzzles on pythonchallenge.com 
    '''
    def __init__(self, url=None):
        self.soup = None
        self.url = url
        
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        self.logger = logging
        self.logger.info('Solving %s located at %s' % (self.__class__.__name__.lower(), url))
        
        requests_cache.install_cache('/tmp/%s' % self.__class__.__name__)
        self.soup = BeautifulSoup(requests.get(self.url).content)


    def solve(self):
        NotImplementedError('This method must be implemented')
        
