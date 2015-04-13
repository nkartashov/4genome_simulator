__author__ = 'nikita_kartashov'

import random

from circular_chromosome import CircularChromosome


def unfold(f, x):
    try:
        while True:
            w, x = f(x)
            yield w
    except:
        raise StopIteration


class Genome(object):
    def __init__(self, block_number, chromosome_number=1, chromosome_constructor=CircularChromosome):
        assert (block_number >= chromosome_number)
        assert (chromosome_number > 0)
        blocks_per_chromosome = block_number / chromosome_number

        def break_helper(value):
            if value <= 0:
                return None
            return min(value, blocks_per_chromosome), value - blocks_per_chromosome

        self._chromosomes = [chromosome_constructor(size) for size in unfold(break_helper, block_number)]

    def perform_random_inversions(self, inversions_number):
        for _ in xrange(inversions_number):
            random_chromosome = random.choice(self._chromosomes)
            random_chromosome.make_random_inversion()
        return self

    def as_grimm(self):
        return '\n'.join(c.as_grimm() for c in self._chromosomes)

