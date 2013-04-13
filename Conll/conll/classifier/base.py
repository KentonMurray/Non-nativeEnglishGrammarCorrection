#!/usr/bin/env python


class BaseClassifier(object):
    def __init__(self):
        self.feature_funcs = []

    def generate_features(self, sentence, position):
        return dict(feature for func in self.feature_funcs
                    for feature in func(sentence, position))

    def train(self, X, Y):
        pass

    def test(self, X):
        pass
