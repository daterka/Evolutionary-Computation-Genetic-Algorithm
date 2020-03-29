from Target_function import function
from math import ceil, log2, pow
from Optimizer import Optimizer
from _Chromosome import Chromosome
from _Configuration import Config

# Number of epochs, just a variable
EPOCHS = 10

# Number of individuals
POPULATION_SIZE = 10

# Target args number
N = 2
# Range of args
X1_RANGE = (-1.5, 4)
X2_RANGE = (-3, 4)

# Solution precision
PRECISION = 6

import numpy as np

def decode_individual(individual, N, B, a, dx):
    arr = (2**np.arange(B, dtype = np.uint64))* dx
    decode_individual = np.sum(individual.reshape((N,B)) * arr,axis=1)
    decode_individual = decode_individual+a
    return decode_individual

def gen_population(P, N, B):
    pop = np.random.randint(0,2, size=(P,N*B))
    return pop


def main():
    # Creating function optimalization model implementing genetic algorithm
    opt = Optimizer(target=function, epochs=EPOCHS, args_num=N, x1_range=X1_RANGE, x2_range=X2_RANGE, precision=PRECISION, population_size=POPULATION_SIZE, type="min")

    # Initiation of pupulation
    opt.initPopulation()
    print(opt.population)

    # TEST : Decoding population's chtomosomes
    for x in opt.population:
        print(x.decode(), ", ", opt.target(x.decode()))

    # Evaluating current population
    opt.evaluate()

    # TEST : Selecting parents
    # Truncation
    best = opt.truncation(2)
    print("TRUNCATION : best = ", best, " decimal : ", best.decode(), "target : ", best.getTargetValue())
    # Tournament
    best = opt.tournament(0.3)
    print("TOURNAMENT : best = ", best, " decimal : ", best.decode(), "target : ",
          best.getTargetValue())

    # Roulette
    opt.normalizePopulation()
    best = opt.roulette()
    print("Roulette : best = ", best, " decimal : ", best.decode(), "target : ",
          best.getTargetValue())

    # Mutation
    print("MUTATION : ", opt.mutate(Chromosome([1,1,1,1,1,1,1,1,1,1], 10), 2, 1))
    print("MUTATION EDGE : ", opt.mutateEdge(Chromosome([1,1,1,1,1,1,1,1,1,1], 10), 2, 1))


    # Generating next generation with truncation
    # print("old pop : ", opt.population)
    # print("old pop decimal : ", [x.getTargetValue() for x in opt.population])
    # opt.nextGen("tournament", 5)
    # print("new pop : ", opt.population)
    # print("new pop decimal : ", [x.getTargetValue() for x in opt.population])

    # Proper optimalization of target function
    opt.initPopulation()
    print("~~~~~~~~~~~~~  OPTIMALIZATION  ~~~~~~~~~~~~~~~")
    print("old pop : ", opt.population)
    print("old pop decimal : ", [x.getTargetValue() for x in opt.population])
    opt.optimize()
    print("new pop : ", opt.population)
    print("new pop decimal : ", [x.getTargetValue() for x in opt.population])

    # GENEREAL TEST
    opt_test = Optimizer(target=function, epochs=100, args_num=N, x1_range=X1_RANGE, x2_range=X2_RANGE, precision=6, population_size=100, type="min")
    opt.optimize()
    print("best = ", opt.getBest().getTargetValue())




main()
