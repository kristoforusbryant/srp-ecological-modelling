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
recr_t, mort_t = [10, 20, 30, 40, 40], [0, 10, 20, 10, 30]

def test_sample_0():
    spec_l = [1, 2, 3, 4]
    lsp = LSP(spec_l, recr_t, mort_t, np.ones((len(spec_l), len(recr_t))), np.ones((len(spec_l), len(recr_t))))
    for _ in np.arange(100):
        t = np.random.choice(len(recr_t))
        assert(lsp.recruit(t) in [1,2,3,4])

def test_sample_1():
    for _ in np.arange(50):
        spec_l = np.random.choice(np.arange(100), 5)
        lsp = LSP(spec_l, recr_t, mort_t, np.ones((len(spec_l), len(recr_t))), np.ones((len(spec_l), len(recr_t))))
        for _ in np.arange(100):
            t = np.random.choice(len(recr_t))
            assert(lsp.recruit(t) in spec_l)

def test_sample_2():
    spec_l = [1, 2, 3, 4]
    recr_probs = np.array([ [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0] ])

    mort_probs = np.ones((len(spec_l), len(recr_t)))

    lsp = LSP(spec_l, recr_t, mort_t, recr_probs, mort_probs)
    for _ in np.arange(100):
        t = np.random.choice(len(recr_t))
        assert(lsp.recruit(t) == 2)

def test_simulate_0():
    spec_l = [1, 2, 3, 4]
    recr_probs = np.array([ [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0] ])

    mort_probs = np.ones((len(spec_l), len(recr_t)))

    lsp = LSP(spec_l, recr_t, mort_t, recr_probs, mort_probs)
    trajectory = np.array(recr_t) - np.array(mort_t)

    M = lsp.simulate()
    assert(M.shape == (4, 5))
    assert(M.sum(axis=0) == trajectory)

    # recruit with probability 1 -> species is always in the landscape
    assert((M[2] > 0).all())
    # recruit with probability 0 -> species is never in the landscape
    for i in [0,1,3]:
        assert((M[i] == 0).all())

def test_simulate_1():
    raise NotImplementedError

# Landscape: GSP
from Landscape import GSP
recr_t, mort_t = [10, 20, 30, 40, 40], [0, 10, 20, 10, 30]

def test_initialise_LSPs():
    gsp = GSP(np.arange(10))
    gsp.initialise_LSPs(4, 5, recr_t, mort_t,
                        np.ones((4, len(recr_t))), np.ones((4, len(recr_t))))

    assert(len(gsp.LSP_list) == 4)
    for i in np.arange(4):
        assert(gsp.LSP_list[i].get_size() == 5)

def test_simulate_GSP_0():
    gsp = GSP(np.arange(10))
    recr_probs = np.zeros((10, len(recr_t)))
    recr_probs[3, :] = 1
    mort_probs = np.ones((10, len(recr_t)))

    gsp.initialise_LSPs(4, 5, recr_t, mort_t, recr_probs, mort_probs)
    trajectory = recr_t - mort_t

    M = gsp.simulate()
    assert(M.shape == (4, 10, 5))
    for i in range(4):
        assert((M[i].sum(axis=0) == trajectory).all())

        if 3 in M.LSP_list[i].species_list:
            for j in M.LSP_list[i].species_list:
                if j == 3:
                    assert((M[i, j, :] > 0).all())
                else:
                    assert((M[i, j, :] == 0).all())

def test_simulate_GSP_1():
    raise NotImplementedError



