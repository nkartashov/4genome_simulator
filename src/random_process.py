__author__ = 'nikita_kartashov'

from copy import copy as deepcopy
import random

from genome import Genome

A, B, C, D = 'A', 'B', 'C', 'D'

TOPOLOGIES = [((A, B), (C, D)),
              ((A, C), (B, D)),
              ((A, D), (C, B))]


def make_random_4genome_process(e1, e2, block_number, chromosome_number, chromosome_constructor):
    left_ancestor = Genome(block_number, chromosome_number, chromosome_constructor)
    right_ancestor = left_ancestor.clone().perform_random_inversions(e1)
    ancestors = dict()
    ancestors['Left'] = left_ancestor
    ancestors['Right'] = right_ancestor
    random_genomes = dict()
    topology = random.choice(TOPOLOGIES)
    (a, b), (c, d) = topology
    random_genomes[a] = left_ancestor.clone().perform_random_inversions(e2)
    random_genomes[b] = left_ancestor.clone().perform_random_inversions(e2)
    random_genomes[c] = right_ancestor.clone().perform_random_inversions(e2)
    random_genomes[d] = right_ancestor.clone().perform_random_inversions(e2)
    return random_genomes, topology, ancestors