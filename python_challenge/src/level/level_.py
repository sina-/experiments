'''
Created on Oct 27, 2013

@author: sina
'''

import requests
import requests_cache
from bs4 import BeautifulSoup

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
        
        cache_path = '/tmp/%s' % self.__class__.__name__
        self.logger.debug('Setting up HTTP cache: %s.sqlite' % cache_path)
        requests_cache.install_cache(cache_path, extension='.sqlite')
        self.logger.debug('Requesting HTTP and dumping to BeautifulSoup')
        self.requests_result = requests.get(self.url)
        self.soup = BeautifulSoup(self.requests_result.text)


    def _echo_success(self, url):
        self.logger.info("Level solved! Next: %s" % url)


    def solve(self):
        NotImplementedError('This method must be implemented')


