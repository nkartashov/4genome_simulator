__author__ = 'nikita_kartashov'

import argparse
from os import makedirs, path, mkdir

from random_process import make_random_4genome_process
from circular_chromosome import Chromosome, CircularChromosome


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out_path', help='Output path', required=True)
    parser.add_argument('-bn', '--block_number', help='Number of blocks in each genome', default=200, type=int)
    parser.add_argument('-cn', '--chromosome_number', help='Number of chromosomes in each genome', default=1, type=int)
    parser.add_argument('-sn', '--simulations_number', help='Number of simulations performed', required=True, type=int)
    parser.add_argument('-l', '--linear', help='Are chromosomes linear?', default=False, action='store_true')
    parser.add_argument('-e1', '--center_distance', help='Center distance', required=True, type=int)
    parser.add_argument('-e2', '--branch_distance', help='Branch distance', required=True, type=int)
    return parser


BLOCK_FILENAME = 'blocks.txt'


def main():
    parser = build_parser()
    args = parser.parse_args()
    out_path = args.out_path
    e1 = args.center_distance
    e2 = args.branch_distance
    block_number = args.block_number
    chromosome_number = args.chromosome_number
    simulations_number = args.simulations_number
    chromosome_constructor = Chromosome if args.linear else CircularChromosome
    if path.exists(out_path) and not path.isdir(out_path):
        print('{0} is not a folder path'.format(out_path))
        exit(1)
    if not path.exists(out_path):
        makedirs(out_path)
    random_genomes = \
        make_random_4genome_process(e1, e2, block_number, chromosome_number, chromosome_constructor)
    for i in xrange(simulations_number):
        simulation_out_path = path.join(out_path, str(i))
        if not path.exists(simulation_out_path):
            mkdir(simulation_out_path)
        with open(path.join(simulation_out_path, BLOCK_FILENAME), 'w') as out_file:
            for name, genome in random_genomes.iteritems():
                out_file.write('>{0}\n'.format(name))
                out_file.write('{0}\n'.format(genome.as_grimm()))


if __name__ == '__main__':
    main()
