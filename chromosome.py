__author__ = 'nikita_kartashov'

import random


class Chromosome(object):
    def __init__(self, size):
        self._blocks = range(1, size + 1)
        self._ending = '$'

    @staticmethod
    def _invert(blocks):
        return [-block for block in reversed(blocks)]

    def _inverted_blocks(self, left, right):
        assert (left >= 0)
        assert (right <= len(self._blocks))
        assert (left < right)
        return self._invert(self._blocks[left: right])

    def make_random_inversion(self):
        left = random.randint(0, len(self._blocks) - 1)
        right = random.randint(left + 1, len(self._blocks))
        self.make_inversion(left, right)

    def make_random_inversions(self, number):
        for _ in xrange(number):
            self.make_random_inversion()

    def make_inversion(self, left, right):
        self._blocks[left: right] = self._inverted_blocks(left, right)

    def __str__(self):
        return self._blocks.__str__()

    def as_grimm(self):
        return ' '.join(map(str, self._blocks)) + ' {0}'.format(self._ending)
