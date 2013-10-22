'''
Created on Oct 17, 2013

@author: sina
'''

import os
import random
import time
import sys

class MemorizeIt(object):
    def __init__(self):
        self.accuracy = 0
        self.overall_accuracy = 0
        self.number_of_runs = 0
        self.sequence_length = None


    def _generate_sequence(self, sequence_length):
        return random.sample(xrange(10), sequence_length)


    def _get_user_input(self, prompt_text=''):
        user_input = raw_input(prompt_text)
        if not user_input or user_input == '':
            self._clear()
            self.accuracy = 0
            self._print_results()
            sys.exit(0)
        try:
            processed_input = [int(i) for i in user_input]
            print processed_input
        except ValueError:
            print('invalid input: %s' % user_input)
            print('enter digits')
            sys.exit(0)
        return processed_input


    def _print_text(self, text, values):
        if type(values) == int or type(values) == float:
            values = [values]
        elif type(values) != list:
            print('invalid values: %s. expecting list of numbers' % values)
        print(text + ' '.join([str(i) for i in values]))


    def _print_results(self, sequence_generated=None, sequence_user_input=None):
        if sequence_generated and sequence_user_input:
            self._print_text('requested sequence: ', sequence_generated)
            self._print_text('requested sequence: ', sequence_user_input)
        self._print_text('accuracy: ', self.accuracy)
        if self.number_of_runs == 0:
            self._print_text('overall accuracy: ', 0)
        else:
            self._print_text('overall accuracy: ', self.overall_accuracy / self.number_of_runs)
        self._print_text('number of runs: ', self.number_of_runs)


    def _suspend(self, delay, echo=True):
        for _ in xrange(delay):
            if echo:
                print(delay - _)
            time.sleep(1)


    def _calculate_score(self, sequence_generated, sequence_user_input):
        if len(sequence_generated) < 1:
            return

        matched_digits = 0
        for i, v in enumerate(sequence_generated):
            if i >= len(sequence_user_input):
                break
            if v == sequence_user_input [i]:
                matched_digits += 1

        self.accuracy = (float(matched_digits) / len(sequence_generated)) * 100

        if len(sequence_user_input) > len(sequence_generated):
            penalty = (len(sequence_user_input) - len(sequence_generated)) / float(len(sequence_generated)) * 100
            if penalty > 100:
                penalty = 100
            self.accuracy -= penalty
            if self.accuracy < 0:
                self.accuracy = 0

        self.overall_accuracy += self.accuracy


    def _clear(self):
        os.system('clear')


    def play(self):
        self._clear()
        self.sequence_length = self._get_user_input('enter sequence length (single digit): ')
        self.sequence_length = self.sequence_length[0]
        self._clear()
        while True:
            sequence_generated = self._generate_sequence(self.sequence_length)
            for digit in sequence_generated:
                print('memorize the following sequence: ' + str(digit))
                self._suspend(1, echo=False)
                self._clear()
            print('repeat the sequence: ')
            sequence_user_input = self._get_user_input()
            self._clear()
            self._calculate_score(sequence_generated, sequence_user_input)
            self.number_of_runs += 1
            self._print_results(sequence_generated, sequence_user_input)
            self._suspend(2)
            self._clear()


if __name__ == '__main__':
    mi = MemorizeIt()
    mi.play()






