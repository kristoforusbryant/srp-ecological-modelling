# Ecological Modelling SRP Week 1


### 0. Software Prerequisites
Please install Python 3 including the following packages: 
- numpy 
- pandas 
- pytest


### 1. Basic Git commands 

First of all, you need a github account. Please make one and send me the name of your account. 

Then you can read the following website to learn about github:

`https://guides.github.com/introduction/git-handbook/`

Please familiarise yourself with the basic operations, especially:

- `git clone` 
- `git fetch` 
- `git merge`
- `git add` 
- `git commit`

Another useful command that is important to learn is opening a pull request. You can learn more about it here:

`https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request`

### 2. Generating Forest Data from Stochastic Processes

Implement the following functions in `Landscape.py`: 

1. `LSP.sample`: Samples a species randomly from the species list in the `species_list` attribute. 

2. `LSP.simulate`: Simulates `t` years of local succession where the overall recruitment and mortality must equal to 
the `recr_trajectory` and  `mort_trajectory` attributes, respectively. At every year, the choice of species to be recruited is a random draw from the species
in the local species pool. Whilst, the choice of species to die at every year is a random draw from the species that are already established in the plot.

The function should return `M`, a `n x t` matrix where `n` is the number of species in the local species pool and `t` is the number of years (speciefied by 
`recr_trajectory` and  `mort_trajectory`). 

3. `GSP.initialise_LSPs`: Initialises local species pools from the list of species in the global species pool. `n` is the number of local pools and `k` is the number of species in each pool. Assume that the local species pool is sampled randomly from the global species pool. 

4. `GSP.simulate`: Simulates `t` years of global succession where the overall recruitment and mortality must equal to 
the `recr_trajectory` and  `mort_trajectory` attributes, respectively.

The function should return `M`, a `n x m x t` matrix where `n` is the number of species in the local species pool, `m` is the number of localities
and `t` is the number of years (speciefied by `recr_trajectory` and  `mort_trajectory`). (Hint: use `LSP.simulate`)


### 3. Testing
Once the implementation is done. Test your implementation with the provided test in `tests.py`. You are encouraged to add additional tests to make sure that your code is correct. 

The test can be run using the command: 

`pytest tests.py`

Once the program is done and tested, stage a pull request on this github. 

### 4. Generating Result 
To save the `n x m x t` matrix output of `GSP.simulate`,  run: 

`python main.py --outfile results/out_matrix.pkl –-params params.json`



