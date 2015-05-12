__author__ = 'nikita_kartashov'

import random

from chromosome import Chromosome


class CircularChromosome(Chromosome):
    def __init__(self, size):
        super(CircularChromosome, self).__init__(size)
        self._ending = '@'

    def make_inversion(self, left, right):
        if left == right:
            right += 1
        if left < right:
            super(CircularChromosome, self).make_inversion(left, right)
        else:
            # assert (1 <= left < len(self._blocks))
            # assert (0 <= right < len(self._blocks) + 1)
            inverted_blocks = self._invert(self._blocks[left:] + self._blocks[:right])
            left_size = len(self._blocks) - left
            self._blocks[left:] = inverted_blocks[:left_size]
            self._blocks[:right] = inverted_blocks[left_size:]

    def make_random_inversion(self):
        left = random.randint(0, len(self._blocks) - 1)
        right = random.randint(0, len(self._blocks) - 1)
        self.make_inversion(left, right)