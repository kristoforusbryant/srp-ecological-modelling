# Ecological Modelling SRP Task 2


### 1. Incorporating Species Recruitment and Mortality Preferences
In the previous task, you have implemented a forest model such that recruitment is random on the set of all LSP species and mortality is
random on all species existing in the plot.

Now, your task is to expand this model to incorporate knowledge about how species. I have expanded the definition of the LSP class in
`Landscape.py` to include to additional attributes: `recr_prob` and `mort_prob`. These `n x t` matrices of **unscaled** probability weights for every
`n` species and for every of the `t` years we simulate.

Implement the following functions in `Landscape.py`:

1. `LSP.recruit`: Samples a species randomly from the species list in the `species_list` attribute according to the recruitment weight at time t.

2. `LSP.kill`: Samples a species randomly (to be killed) from the existing species according to the mortality weight at time t.

3. `LSP.simulate`: Simulates `t` years of local succession where the overall recruitment and mortality must equal to
the `recr_trajectory` and  `mort_trajectory` attributes, respectively. At every year, the choice of species to be recruited is a random draw weighted by `recr_prob` attribute at the particular year. The choice of species to die at every year is a random draw from the species that are already established in the plot weighted by `mort_prob`.

4. `GSP.initialise_LSPs`: Update the previous version to incorporate arguments `recr_prob` and `mort_prob`.

### 2. Testing
Similar to before, once the implementation is done, test your implementation with the provided test in `test.py`.

5. Implement `test_simulate_1` and `test_simulate_GSP_1` which adds into the test suited. You are encouraged to add even more tests.

Once the implementation is done, test your implementation with the provided test in `test.py`. You are encouraged to add additional tests to make sure that your code is correct.

The test can be run using the command:

`pytest test.py`

Once the program is done and tested, stage a pull request on this github.

### 3. Generating Result
This data is provided in `data/recr_data.csv` and `data/mort_data.csv`. Refer to `main.py` to see how this dataset is incorporated to the program.

To save the `m x n x t` matrix output of `GSP.simulate`,  run:
`python main.py --outfile results/out_matrix.pkl –-params params.json`



