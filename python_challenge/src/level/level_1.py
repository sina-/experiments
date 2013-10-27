'''
Created on Oct 27, 2013

@author: sina
'''

from level.level_ import Level
from string import maketrans, translate

class Level1(Level):
    def __init__(self):
        super(Level1, self).__init__(url='http://www.pythonchallenge.com/pc/def/map.html')

    def _decode(self, text):
        translation_table = maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
        return translate(str(text), translation_table)

    def solve(self):
        coded_text = self.soup.br.font.get_text()
        self.logger.info('Coded text: %s' % coded_text)
        self.logger.info('Decoded text: %s' % self._decode(coded_text))
        self.logger.info('Applied on the url (only the word map): %s' % self._decode('map'))
        self.logger.info('Next level url: %s' % self.url.replace('map', self._decode('map')))
        