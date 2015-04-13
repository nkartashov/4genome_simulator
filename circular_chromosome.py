__author__ = 'nikita_kartashov'

import random

from chromosome import Chromosome


class CircularChromosome(Chromosome):
    def __init__(self, size):
        super(CircularChromosome, self).__init__(size)

    def make_inversion(self, left, right):
        if left < right:
            super(CircularChromosome, self).make_inversion(left, right)
        else:
            assert (1 <= left < len(self._blocks))
            assert (0 <= right < len(self._blocks) + 1)
            inverted_blocks = self._invert(self._blocks[left:] + self._blocks[:right])
            left_size = len(self._blocks) - left
            self._blocks[left:] = inverted_blocks[:left_size]
            self._blocks[:right] = inverted_blocks[left_size:]

    def make_random_inversion(self):
        if bool(random.getrandbits(1)):
            # left < right
            super(CircularChromosome, self).make_random_inversion()
        else:
            # left > right
            left = random.randint(1, len(self._blocks) - 1)
            right = random.randint(0, left - 1)
            self.make_inversion(left, right)

    def make_random_inversions(self, number):
        for _ in xrange(number):
            self.make_random_inversion()