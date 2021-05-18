# Ecological Modelling Week 1

Described in this repository the _ tasks that you need to do this week. 

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

1. `LSP.sample`: samples a species randomly from the species list in the `species_list` attribute. 

2. `LSP.simulate`: simulates `t` years of forest succession where the overall recruitment and mortality must equal to 
the `recr_trajectory` and  `mort_trajectory` attributes, respectively. At every year, the choice of species to be recruited is a random draw from the species
in the local species pool. Whilst, the choice of species to die at every year is a random draw from the species that are already established in the plot.

The function should return `M`, a `n x t` matrix where `n` is the number of species in the local species pool and `t` is the number of years (speciefied by 
`recr_trajectory` and  `mort_trajectory`). 

3. `GSP.initialise_LSPs`: initialises local species pools from the list of species in the global species pool



