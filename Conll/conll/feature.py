#!/usr/bin/env python

def is_first_word(sentence, position):
    return [('isFirstWord', int(position == 0))]

def is_last_word(sentence, position):
    return [('isLastWord', int(position == len(sentence) - 1))]

