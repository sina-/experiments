'''
Created on Oct 27, 2013

@author: sina
'''

from level.level_ import Level

class Level0(Level):
    def __init__(self):
        super(Level0, self).__init__(url='http://www.pythonchallenge.com/pc/def/0.html')

    def solve(self):
        self.logger.info(self.soup.p.contents)
        solution = 2**23 
        self.logger.info('Inside image -> 2^23 -> %s' % solution)
        self.logger.info('Next level url: %s' % self.url.replace('0', str(solution)))
