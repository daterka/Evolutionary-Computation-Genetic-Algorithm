from Target_function import function
from math import floor
import numpy as np
import random
from _Configuration import Config


class Selection:

    def sortedPopulation(self):
        return sorted(self.population, key=lambda ch: ch.getTargetValue(), reverse=False)

    def truncation(self, trunc=0.3):
        if (trunc % 1 != 0):
            trunc = floor(self.population_size * trunc)

        parents = self.sortedPopulation()
        # TODO do it with slice
        if (self.type == "min"):
            return random.choice(parents[:trunc])
        else:
            return random.choice(parents[trunc:])

    def normalizePopulation(self):
        # TODO is repeated evetytime, recode more efficient

        normalized_population = [x.getTargetValue() for x in self.population]
        # TODO calculate in more statistical manner
        bias = 0.05
        shilft = abs(self.sortedPopulation()[0].getTargetValue()) + bias
        targets_sum = 0
        for i in range(self.population_size):
            normalized_population[i] = 1/(normalized_population[i] + shilft)
            targets_sum += normalized_population[i]

        probabilities = []
        distribiution = 0
        # TODO not store in Config
        Config.cumulative_distribution = []
        for x in normalized_population:
            probability = x/targets_sum
            probabilities.append(probability)
            distribiution += probability
            self.cumulative_distribution.append(distribiution)

    def roulette(self, param=None):
        ptr = random.uniform(0, 1)
        for i in range(self.population_size):
            if ptr <= self.cumulative_distribution[i]:
                return self.population[i]
        else:
            print("ERROR")

    def tournament(self, group_size=0.2):
        if (group_size % 1 != 0):
            group_size = floor(self.population_size * group_size)

        parents = []

        # TODO using random best fitted elems may be missed
        # TODO condition shuld be handled by fit method depending on type param
        tournament_population = random.sample(self.population, group_size)  # sample - not repeats elems or choises - repeats elems
        best = min(tournament_population, key=lambda ch: ch.getTargetValue())

        return best

