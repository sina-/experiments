'''
Created on Oct 27, 2013

@author: sina
'''

class Level(object):
    '''
    Abstract class to solve puzzles on pythonchallenge.com 
    '''
    def __init__(self):
        print(__class__.__name__)


    def solve(self):
        NotImplementedError('This method must be implemented')
