'''
Created on Oct 27, 2013

@author: sina
'''

from level.level_ import Level

class Level1(Level):
    def __init__(self):
        super(Level1).__init__(type(self))

    def solve(self):
        pass
        