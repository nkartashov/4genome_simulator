__author__ = 'nikita_kartashov'

import random
from copy import copy


class Chromosome(object):
    def __init__(self, size):
        self._blocks = range(1, size + 1)
        self._ending = '$'
        self._possible_splits = Chromosome._possible_splits

    def clone(self):
        c = Chromosome(len(self._blocks))
        c._blocks = copy(self._blocks)
        return c

    def __eq__(self, other):
        return self._blocks == other._blocks

    @staticmethod
    def generate_possible_splits(size):
        possible_splits = []
        for left in xrange(0, size):
            for right in xrange(left + 1, size + 1):
                possible_splits.append((left, right))
        return possible_splits

    @staticmethod
    def _invert(blocks):
        return [-block for block in reversed(blocks)]

    def _inverted_blocks(self, left, right):
        assert (left >= 0)
        assert (right <= len(self._blocks))
        assert (left < right)
        return self._invert(self._blocks[left: right])

    def make_random_inversion(self):
        left, right = random.choice(self._possible_splits)
        self.make_inversion(left, right)

    def make_inversion(self, left, right):
        self._blocks[left: right] = self._inverted_blocks(left, right)

    def __str__(self):
        return self._blocks.__str__()

    def as_grimm(self):
        return ' '.join(map(str, self._blocks)) + ' {0}'.format(self._ending)