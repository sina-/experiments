'''
Created on Nov 2, 2013

@author: sina
'''
from level.level_ import Level
from collections import Counter

class Level2(Level):
    def __init__(self):
        super(Level2, self).__init__(url='http://www.pythonchallenge.com/pc/def/ocr.html')


    def solve(self):
        self.logger.info("Text from the page: " + self.soup.get_text())
        self.logger.info('Retrieving obfuscated text...')
        r = self.requests_result.content
        obfuscated_text = r[r.rfind('<!--')+4:]
        self.logger.debug(obfuscated_text[:500] + ' ...')

        char_count = Counter(obfuscated_text)
        self.logger.info('Looking for rare characters...')
        self.logger.info('Rare characters: %s' % [i for i,v in char_count.iteritems() if v == 1])
        self.logger.info("Rare characters are anagram for: 'equality'")
        self._echo_success(self.url.replace('ocr', 'equality'))
