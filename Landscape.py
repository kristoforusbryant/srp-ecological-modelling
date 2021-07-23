import numpy as np
class LSP:
    """Local Species Pool
    """
    def __init__(self, species_list, recr_trajectory, mort_trajectory, recr_prob, mort_prob):
        self.species_list = species_list
        self.recr_trajectory = recr_trajectory
        self.mort_trajectory = mort_trajectory
        self.recr_prob = recr_prob
        self.mort_prob = mort_prob

    def get_size(self):
        return len(self.species_list)

    def sample(self):
        """
        Sample randomly from species_list
        """
        raise NotImplementedError

    def recruit(self, t):
        """
        Sample randomly from the species_list according to the recruitment weight at time t
        """
        raise NotImplementedError

    def kill(self, a, t):
        """
        Sample randomly from a according to the recruitment weight at time t
        """
        raise NotImplementedError

    def simulate(self):
        n = len(self.species_list) # number of species
        t = len(self.mort_trajectory) # time
        M = np.zeros((n, t)) # Empty 2-dimensional matrix

        raise NotImplementedError

        return M


class GSP:
    """Global Species Pool
    """
    def __init__(self, species_list):
        self.species_list = species_list
        self.LSP_list = []

    def initialise_LSPs(self, n, k, recr_t, mort_t, recr_prob, mort_prob):
        """ Initialise LSP_lists
        Args:
            n (int): number of LSPs
            k (int): number of species in each LSPs
            recr_t(int list): number of total recruitment to an LSP for every year
            mort_t(int list): number of total mortality to an LSP for every year
            recr_prob(float list): unscaled recruitment weights of each species in the LSP for every year
            mort_prob(float list): unscaled mortality weights of each species in the LSP for every year

        Remark: Assume that the recr_t and mort_t are the same for every LSPs in LSP_list
        """
        raise NotImplementedError

    def simulate(self):
        """Simulate succession according to a fixed trajectory
        """
        n = len(self.species_list) # number of species
        m = len(self.LSP_list) # number of localities
        t = len(self.LSP_list[0].mort_trajectory) # time
        M = np.zeros((n, m, t)) # Empty 3-dimensional matrix

        raise NotImplementedError # Hint: use LSP.simulate

        return M

