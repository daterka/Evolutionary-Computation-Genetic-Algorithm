from _Configuration import Config
from _Chromosome import Chromosome
from _Selection import Selection
from _Crossover import Crossover
from _Inversion import Inversion
from _Mutation import Mutation
from math import ceil, floor, log2, sin
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import random

# Module scopes
class Optimizer(Config, Selection, Crossover, Inversion, Mutation):
    def __init__(self, epochs=10, population_size=10, target=None, precision=6, type="min", args_num=1, x1_range=(-1, 1), x2_range=(-1, 1)):
        Config.epochs = epochs
        Config.population_size = population_size
        Config.target = target
        Config.args_num = args_num
        Config.precision = precision
        Config.type = type;
        Config.x1_a, Config.x1_b = x1_range
        Config.x2_a, Config.x2_b = x2_range
        Config.x1_length = self.argLength(abs(self.x1_b - self.x1_a))
        Config.x2_length = self.argLength(abs(self.x2_b - self.x2_a))
        Config.chromosome_length = self.x1_length + self.x2_length

    # TODO handling custom numbers of agrs
    def argLength(self, domain_len):
        return (ceil(log2(domain_len * pow(10, self.precision)) + log2(1)))

    def chromosomeLength(self):
        x1_length = self.argLength(abs(self.x1_b - self.x1_a))
        x2_length = self.argLength(abs(self.x2_b - self.x2_a))
        return x1_length + x2_length

    def initPopulation(self):
        # TODO make more readable
        self.population = [Chromosome([random.randrange(2) for x in range(self.chromosome_length)], self.chromosome_length) for x in
                           range(self.population_size)]

    # TODO format
    def evaluate(self):
        for chromosome in self.population:
            target_val = Config.target(chromosome.decode())
            chromosome.setTargetValue(target_val)

    # TODO todo..
    def validateChromosome(self):
        pass

    # TODO mote suitable method name
    def reproduction(self, selection, selection_parameter, crossover, mutation, survival_rate):
        offspring = []
        mutation, mutation_n, mutation_prob = mutation

        if selection == self.roulette():
            self.normalizePopulation()

        while len(offspring) < self.population_size-floor(self.population_size*survival_rate):
            parent_1 = selection(selection_parameter)
            parent_2 = selection(selection_parameter)

            child_1, child_2 = crossover(parent_1, parent_2)

            child_1 = mutation(child_1, mutation_n, mutation_prob)
            child_2 = mutation(child_2, mutation_n, mutation_prob)
            # TODO inlude both childs or just best ??
            offspring.append(child_1)
            offspring.append(child_2)

        best_indx = floor(self.population_size*survival_rate)
        current_fittest = self.sortedPopulation()[:best_indx]

        nextGeneration = current_fittest + offspring

        return nextGeneration

    def nextGen(self, selection, selection_parameter, crossover, mutation, survival_rate):
        self.evaluate()
        # TODO add exceptions if not enough params provided

        self.population = self.reproduction(selection, selection_parameter, crossover, mutation, survival_rate)

    def getBest(self):
        return self.best

    def optimize(self, selection="roulette", selection_parameter = 0.2, crossover="threepoint", mutation=("random", 1, 0.1), survival_rate = 0.1):
        epochs_counter = 0

        if selection == "truncation" or selection == 0:
            selection = self.truncation
        elif selection == "tournament" or selection == 1:
            selection = self.tournament
        else:
            selection = self.roulette

        if crossover == "onepoint" or crossover == 0:
            crossover = self.cross_onepoint
        elif crossover == "twopoint" or crossover == 1:
            crossover = self.cross_twopoint
        elif crossover == "threepoint"  or crossover == 2:
            crossover = self.cross_threepoint
        else:
            crossover = self.cross_united

        mutation, mutation_n, mutation_prob = mutation

        if mutation == "edge":
            mutation = self.mutateEdge
        else:
            mutation = self.mutate

        mutation = (mutation, mutation_n, mutation_prob)


        while(epochs_counter < self.epochs):
            self.nextGen(selection, selection_parameter, crossover, mutation, survival_rate)
            epochs_counter += 1

        self.evaluate()

        self.best = self.truncation(1)
