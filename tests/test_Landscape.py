import numpy as np
import sys, os

currdir = os.path.dirname(__file__)
sys.path.append(os.path.dirname(currdir))
print(os.path.dirname(currdir))
print(sys.path)

# Parser
import Parser
def test_parser():
    """ test that parser returns the correct types
    """
    sys_args = ['--outfile', 'results/out_matrix.pkl', '--params', 'params.json']
    parser = Parser.Parser(sys_args)
    assert(isinstance(parser.args.outfile, str))
    assert(isinstance(parser.args.params, str))

# Landscape: LSP
# test_sample_0 and test_sample_1 does not change from task-01
from Landscape import LSP
def test_sample_0():
    lsp = LSP([1,2,3,4], [10, 20, 30, 40, 40], [0, 10, 20, 10, 30], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
    for _ in np.arange(100):
        assert(lsp.sample() in [1,2,3,4])

def test_sample_1():
    for _ in np.arange(50):
        l = np.random.choice(np.arange(100), 5)
        lsp = LSP(l, [10, 20, 30, 40, 40], [0, 10, 20, 10, 30], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
        for _ in np.arange(100):
            assert(lsp.sample() in l)

def test_sample_2():
    lsp = LSP([1,2,3,4], [], [], recr_prob=[0, 0, 1, 0], mort_prob=[1, 1, 1, 1])
    for _ in np.arange(100):
        assert(lsp.sample() == 3)

def test_simulate_0():
    lsp = LSP([1,2,3,4], [10, 20, 30, 40, 40], [0, 10, 20, 10, 30],
              recr_prob=[0, 0, 1, 0], mort_prob=[1,1,1,1])
    trajectory = np.array([10, 20, 30, 40, 40]) - np.array([0, 10, 20, 10, 30])
    M = lsp.simulate()
    assert(M.shape == (4, 5))
    assert(M.sum(axis=0) == trajectory)
    assert((M[2] > 0).all())
    for i in [0,1,3]:
        assert((M[i] == 0).all())

def test_simulate_1():
    raise NotImplementedError

# Landscape: GSP
from Landscape import GSP
def test_initialise_LSPs():
    gsp = GSP(np.arange(10))
    gsp.initialise_LSPs(4, 5, [10, 20, 30, 40, 40], [0, 10, 20, 10, 30],
                        [1, 1, 1, 1], [1, 1, 1, 1])
    assert(len(gsp.LSP_list) == 4)
    for i in np.arange(4):
        assert(gsp.LSP_list[i].get_size() == 5)

def test_simulate_GSP_0():
    gsp = GSP(np.arange(10))
    gsp.initialise_LSPs(4, 5, [10, 20, 30, 40, 40], [0, 10, 20, 10, 30],
                        recr_prob=[0, 0, 1, 0], mort_prob=[1, 1, 1, 1])
    trajectory = np.array([10, 20, 30, 40, 40]) - np.array([0, 10, 20, 10, 30])
    M = gsp.simulate()

    assert(M.shape == (4, 5, 5))
    for i in range(4):
        assert((M[i].sum(axis=0) == trajectory).all())
        assert((M[i, 2, :] > 0).all()) # recruit with probability 1 -> species is always in the landscape
        for j in [0, 1, 3]:
            assert((M[i, j, :] == 0).all()) # recruit with probability 0 -> species is never in the landscape

def test_simulate_GSP_1():
    raise NotImplementedError



