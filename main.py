"""Simulating Randomly

This script allows the user to obtain the random simulation result of
species specific trajectories.

The script should be run as:
`python main.py --outfile results/out_matrix.pkl –-params params.json`

This script requires the packages `numpy`, and `pandas` to be
installed within the Python environment you are running this script in.

Listed here are the arguments of the program:
    --outfile, path to file that will contain the result
    --params, input parameters

Author: Kristoforus Bryant Odang
"""

import sys
import Parser
import json
from Landscape import GSP
import pandas as pd
import pickle

def main():
    # Parsing user-given arguments
    parser = Parser.Parser(sys.argv[1:])

    with open(parser.args.params) as handle:
        param = json.load(handle)

    species_list = list(range(param['n_species']))
    trajectories = pd.read_csv(param["overall_trajectory_path"], index_col=0)

    # Initialising landscape
    gsp = GSP(species_list)
    gsp.initialise_LSPs(param["n_LSPs"], param["local_pool_size"],
                        trajectories["recr"], trajectories["mort"])

    # Running simulation
    res = gsp.simulate()

    with open(parser.args.outfile, 'wb') as handle:
        pickle.dump(res, handle)

if __name__ == "__main__":
    main()