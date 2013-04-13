#!/usr/bin/env python

from conll.classifier.base import BaseClassifier
import conll.feature as feature

class NnClassifier(BaseClassifier):
    def __init__(self):
        super(NnClassifier, self).__init__()

        self.feature_funcs = [
            feature.is_first_word,
            feature.is_last_word,
        ]
