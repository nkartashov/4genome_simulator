__author__ = 'nikita_kartashov'

import random
from sys import argv
from os import path, makedirs

from simulate import simulate
from circular_chromosome import CircularChromosome


SIMULATIONS_PER_SETUP = 1000
BLOCKS_PER_GENOME = 200
CHROMOSOME_NUMBER = 1

# Outputs the range which looks like 5, 10, 20, ..., x
def five_to_x(x):
    return [5] + range(10, x + 10, 10)


FIVE_TO_FORTY = five_to_x(40)
FIVE_TO_SIXTY = five_to_x(60)

PARAMETER_GROUPS = [
    # First group: both e1 & e2 are 5, 10 to 40
    (FIVE_TO_FORTY, FIVE_TO_FORTY),
    # Second group: e1 = 1 to 5, e2 = 5, 10 to 60
    (range(1, 6), FIVE_TO_SIXTY)]

if __name__ == '__main__':
    if len(argv) == 1:
        print('No output path specified')
        exit(1)
    output_path = argv[1]
    random.seed()
    for i, group in enumerate(PARAMETER_GROUPS):
        e1s, e2s = group
        for e1 in e1s:
            for e2 in e2s:
                if not path.exists(output_path):
                    makedirs(output_path)
                group_e1_e2_folder_path = path.join(output_path,
                                                    '_'.join([str(i), str(e1), str(e2)]))
                simulate(e1, e2, BLOCKS_PER_GENOME, CHROMOSOME_NUMBER, CircularChromosome, SIMULATIONS_PER_SETUP,
                         group_e1_e2_folder_path)