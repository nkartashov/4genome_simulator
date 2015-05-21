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
    def __init__(self, block_number=0, chromosome_number=1, chromosome_constructor=CircularChromosome):
        self._chromosomes = None
        if block_number == 0:
            return
        assert (block_number >= chromosome_number)
        assert (chromosome_number > 0)
        blocks_per_chromosome = block_number / chromosome_number

        def break_helper(value):
            if value <= 0:
                return None
            return min(value, blocks_per_chromosome), value - blocks_per_chromosome

        self._chromosomes = [chromosome_constructor(size) for size in unfold(break_helper, block_number)]

    def __eq__(self, other):
        return all(l == r for l, r in zip(self._chromosomes, other._chromosomes))

    def perform_random_inversions(self, inversions_number):
        for _ in xrange(inversions_number):
            random_chromosome = random.choice(self._chromosomes)
            random_chromosome.make_random_inversion()
        return self

    def clone(self):
        g = Genome()
        g._chromosomes = list(c.clone() for c in self._chromosomes)
        return g

    def as_grimm(self):
        return '\n'.join(c.as_grimm() for c in self._chromosomes)

