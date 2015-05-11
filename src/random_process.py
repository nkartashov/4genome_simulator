__author__ = 'nikita_kartashov'

from copy import deepcopy

from genome import Genome


def make_random_4genome_process(e1, e2, block_number, chromosome_number, chromosome_constructor):
    left_ancestor = Genome(block_number, chromosome_number, chromosome_constructor)
    right_ancestor = deepcopy(left_ancestor).perform_random_inversions(e1)
    random_genomes = dict()
    random_genomes['A'] = deepcopy(left_ancestor).perform_random_inversions(e2)
    random_genomes['B'] = deepcopy(left_ancestor).perform_random_inversions(e2)
    random_genomes['C'] = deepcopy(right_ancestor).perform_random_inversions(e2)
    random_genomes['D'] = deepcopy(right_ancestor).perform_random_inversions(e2)
    random_genomes['Left'] = left_ancestor
    random_genomes['Right'] = right_ancestor
    return random_genomes