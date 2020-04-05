from Target_function import function
from math import ceil, log2, pow
from Optimizer import Optimizer
from _Chromosome import Chromosome
from _Configuration import Config

# Number of epochs, just a variable
EPOCHS = 100

# Number of individuals
POPULATION_SIZE = 100

# Target args number
N = 2
# Range of args
X1_RANGE = (-1.5, 4)
X2_RANGE = (-3, 4)

# Solution precision
PRECISION = 6

# Optimalization type
opt_type = 0 # minimalization

# selection
selection = "roulette"
selection_parameter = None

# crossover
crossover = "threepoint"
crossover_prob = 0.9

# mutation
mutation = "random"
mutation_n = 3
mutation_prob = 0.1

# inversion
inversion_prob = 0.05

def main():
   

    # GENEREAL TEST
    opt_test = Optimizer(target=function, args_num=N, x1_range=X1_RANGE, x2_range=X2_RANGE,
                         precision=PRECISION, epochs=EPOCHS, population_size=POPULATION_SIZE, type=0)

    opt_test.initPopulation()

    opt_test.optimize(selection=(selection, selection_parameter),
                         crossover=(crossover, crossover_prob),
                         mutation=(mutation, mutation_n, mutation_prob),
                        inversion_prob=inversion_prob)

    print("best = ", opt_test.getBest().getTargetValue())




main()
