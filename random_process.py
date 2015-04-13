__author__ = 'nikita_kartashov'

import random

from genome import Genome
from copy import deepcopy


def make_random_4genome_process(e1, e2, block_number, chromosome_number, chromosome_constructor):
    random.seed()
    center_genome = Genome(block_number, chromosome_number, chromosome_constructor)
    distance_to_left = e1 / 2
    distance_to_right = e1 - distance_to_left
    left_ancestor = deepcopy(center_genome).perform_random_inversions(distance_to_left)
    right_ancestor = center_genome.perform_random_inversions(distance_to_right)
    random_genomes = dict()
    random_genomes['A'] = deepcopy(left_ancestor).perform_random_inversions(e2)
    random_genomes['B'] = left_ancestor.perform_random_inversions(e2)
    random_genomes['C'] = deepcopy(right_ancestor).perform_random_inversions(e2)
    random_genomes['D'] = right_ancestor.perform_random_inversions(e2)
    return random_genomes