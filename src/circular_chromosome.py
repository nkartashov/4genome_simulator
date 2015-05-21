__author__ = 'nikita_kartashov'

from copy import copy

from chromosome import Chromosome


class CircularChromosome(Chromosome):
    def __init__(self, size):
        super(CircularChromosome, self).__init__(size)
        self._ending = '@'
        self._possible_splits = CircularChromosome._possible_splits

    def clone(self):
        c = CircularChromosome(len(self._blocks))
        c._blocks = copy(self._blocks)
        return c

    @staticmethod
    def generate_possible_splits(size):
        possible_splits = []
        for left in xrange(1, size):
            for right in xrange(1, left):
                possible_splits.append((left, right))
        return possible_splits

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


def prepare_chromosomes(size):
    Chromosome._possible_splits = Chromosome.generate_possible_splits(size)
    CircularChromosome._possible_splits = CircularChromosome.generate_possible_splits(size)