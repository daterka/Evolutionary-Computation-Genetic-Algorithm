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
    def __init__(self, epochs=10, population_size=10, target=None, precision=6, type=0, args_num=1, x1_range=(-1, 1), x2_range=(-1, 1)):
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
    def reproduction(self, selection, selection_parameter, crossover, crossover_prob, mutation, mutation_n, mutation_prob, survival_rate, inversion_prob):
        offspring = []

        if selection == self.roulette:
            self.normalizePopulation()

        # TODO indexes of population
        while len(offspring) < self.population_size-floor(self.population_size*survival_rate):
            parent_1 = selection(selection_parameter)
            parent_2 = selection(selection_parameter)

            child_1, child_2 = crossover(parent_1, parent_2, crossover_prob)

            child_1 = mutation(child_1, mutation_n, mutation_prob)
            child_2 = mutation(child_2, mutation_n, mutation_prob)

            child_1 = self.invert(child_1, inversion_prob)
            child_2 = self.invert(child_2, inversion_prob)
            # TODO inlude both childs or just best ??
            offspring.append(child_1)
            offspring.append(child_2)

        best_indx = floor(self.population_size*survival_rate)
        current_fittest = self.sortedPopulation()[:best_indx]

        nextGeneration = current_fittest + offspring

        return nextGeneration

    def nextGen(self, selection, selection_parameter, crossover, crossover_prob, mutation, mutation_n, mutation_prob, survival_rate, inversion_prob):
        self.evaluate()
        # TODO add exceptions if not enough params provided

        self.population = self.reproduction(selection, selection_parameter, crossover, crossover_prob, mutation, mutation_n, mutation_prob, survival_rate, inversion_prob)

    def getBest(self):
        return self.best

    def optimize(self, selection=("roulette", 0.2),
                 crossover=("threepoint", 0.3),
                 mutation=("random", 1, 0.1),
                 survival_rate = 0.1, inversion_prob = 0.05):

        epochs_counter = 0

        selection, selection_parameter = selection
        if selection == "truncation" or selection == 0:
            selection = self.truncation
        elif selection == "tournament" or selection == 1:
            selection = self.tournament
        else:
            selection = self.roulette

        crossover, crossover_prob = crossover
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

        while(epochs_counter < self.epochs):
            self.nextGen(selection, selection_parameter, crossover, crossover_prob, mutation, mutation_n, mutation_prob, survival_rate, inversion_prob)
            epochs_counter += 1

        self.evaluate()

        self.best = self.truncation(1)


    def marekBest(self, best):
        self.ax.scatter(best.decode(), best.getTargetValue(), c='y', marker='o')
        plt.clf()
        plt.show()

    def updateTargetPlot(self):
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator, FormatStrFormatter
        import matplotlib.pyplot as plt
        x = []
        y = []
        z = []
        for chrom in self.population:
            x_val, y_val = chrom.decode()
            x.append(x_val)
            y.append(y_val)
            z.append(chrom.getTargetValue())

        self.ax.scatter(x, y, z, c='r', marker='o')
        plt.clf()
        plt.show()

    def drawTarget(self):
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator, FormatStrFormatter
        import matplotlib.pyplot as plt


        x = []
        y = []
        z = []
        for chrom in self.population:
            x_val, y_val = chrom.decode()
            x.append(x_val)
            y.append(y_val)
            z.append(chrom.getTargetValue())

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.view_init(azim=30)
        self.ax.scatter(x, y, z, c='r', marker='o')

        plt.show()
