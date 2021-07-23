import numpy as np
class LSP:
    """Local Species Pool
    """
    def __init__(self, species_list, recr_trajectory, mort_trajectory):
        self.species_list = species_list
        self.recr_trajectory = recr_trajectory
        self.mort_trajectory = mort_trajectory

    def get_size(self):
        return len(self.species_list)

    def sample(self):
        """
        Sample randomly from species_list
        """
        return np.random.choice(self.species_list)

    def simulate(self):
        n = len(self.species_list) # number of species
        t = len(self.mort_trajectory) # time
        M = np.zeros((n, t)) # empty 2-dimensional matrix

        for generation in np.arange(t):
            temp = M[:, generation]

            # Death
            for _ in np.arange(self.mort_trajectory[generation]):
                n_index = np.random.choice(np.where(temp)[0])
                temp[n_index] -= 1

            # Recruitment
            for _ in np.arange(self.recr_trajectory[generation]):
                n_index = np.random.choice(np.arange(n))
                temp[n_index] += 1

            M[:, generation] = temp

            if generation != (t - 1):
                M[:, generation + 1] = temp

        return M


class GSP:
    """Global Species Pool
    """
    def __init__(self, species_list):
        self.species_list = species_list
        self.LSP_list = []

    def initialise_LSPs(self, n, k, recr_t, mort_t):
        """ Initialise LSP_lists
        Args:
            n (int): number of LSPs
            k (int): number of species in each LSPs
            recr_t(int list): number of total recruitment to an LSP for every year
            mort_t(int list): number of total mortality to an LSP for every year
        Remark: Assume that the recr_t and mort_t are the same for every LSPs in LSP_list
        """
        for i in np.arange(n):
            lsp_list = np.random.choice(self.species_list, k, replace=False)
            self.LSP_list.append(LSP(lsp_list, recr_t, mort_t))

    def simulate(self):
        """Simulate succession according to a fixed trajectory
        """
        n = len(self.species_list) # number of species
        m = len(self.LSP_list) # number of localities
        t = len(self.LSP_list[0].mort_trajectory) # time
        M = np.zeros((m, n, t)) # empty 3-dimensional matrix

        for i in np.arange(m):
            M[i] = self.LSP_list[i].simulate()

        return M