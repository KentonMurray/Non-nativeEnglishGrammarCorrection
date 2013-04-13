#!/usr/bin/env python

'''
Feature functions take as input a `Sentence` object and a int position.
They should return a list of tuples, where the 1st element of the tuple
contains the name of the feature, and the 2nd element of the tuple contains the
value of the feature
'''


def is_first_word(sentence, position):
    return [('isFirstWord', int(position == 0))]


def is_last_word(sentence, position):
    return [('isLastWord', int(position == len(sentence) - 1))]
