__author__ = 'nikita_kartashov'

import subprocess
from sys import argv
from os import path, mkdir

SIMULATIONS_PER_SETUP = 1000
BLOCKS_PER_GENOME = 200
e1s = range(1, 6)  # 1 to 5
e2s = [5] + range(10, 70, 10)  # 5, 10 to 60

if __name__ == '__main__':
    if len(argv) == 1:
        print('No output path specified')
        exit(1)
    output_path = argv[1]
    for e1 in e1s:
        for e2 in e2s:
            e1_e2_folder_path = path.join(output_path, '_'.join([str(e1), str(e2)]))
            if not path.exists(e1_e2_folder_path):
                mkdir(e1_e2_folder_path)
            args = ['python',
                    'simulate.py',
                    '-o', '{0}'.format(e1_e2_folder_path),
                    '-sn', '{0}'.format(SIMULATIONS_PER_SETUP),
                    '-e1', '{0}'.format(e1),
                    '-e2', '{0}'.format(e2)]
            subprocess.call(args)