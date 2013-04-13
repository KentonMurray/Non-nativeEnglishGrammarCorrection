#!/usr/bin/env python

class Sentence:
    def __init__(self, tokens=[], poss=[], dpheads=[], dprels=[], synts=[]):
        assert len(tokens) == len(poss) == len(dpheads) == len(dprels) == len(synts)
        self.tokens = tokens
        self.poss = poss
        self.dpheads = dpheads
        self.dprels = dprels
        self.synts = synts

    def __iter__(self):
        return iter(zip(self.tokens, self.poss, self.dpheads, self.dprels, self.synts))

    def __len__(self):
        return len(self.tokens)

    def __repr__(self):
        return ('Sentence(tokens={self.tokens} '
                '| poss={self.poss} | dpheads={self.dpheads} '
                '| dprels={self.dprels} | synts={self.synts})').format(self=self)

