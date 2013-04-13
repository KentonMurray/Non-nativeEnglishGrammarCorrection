#!/usr/bin/env python

from classifier.base import BaseClassifier
import feature as feature


class PrepClassifier(BaseClassifier):
    def __init__(self):
        super(PrepClassifier, self).__init__()

        self.feature_funcs = [
            feature.is_first_word,
            feature.is_last_word,
        ]
