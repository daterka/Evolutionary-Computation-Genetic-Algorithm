from math import floor
import random

from src.logic._Chromosome import Chromosome
from src.logic.configuration._Configuration import Config


class Selection:
    def sortedPopulation(self):
        return sorted(self.population, key=lambda ch: ch.getTargetValue(), reverse=False)

    def truncation(self, trunc=0.3):
        if (trunc % 1 != 0):
            trunc = floor(self.population_size * trunc)
        else:
            trunc = int(trunc)

        parents = self.sortedPopulation()
        # TODO do it with slice
        if (self.type == 0):
            return parents[:trunc]
        else:
            return parents[trunc:]

    def normalizePopulation(self):
        # TODO is repeated evetytime, recode more efficient
        # TODO WATCH FOR THIS OPT TYPE VAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if(self.type == 0):
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
        else:
            pass

    def roulette(self):
        # TODO ptr could be 1, cum distro is always less than 1 : 10e-16
        ptr = random.uniform(0, 1)
        # print("...............log : roulette : cum_dist= ", self.cumulative_distribution)
        # print("...............log : roulette : ptr = ", ptr)
        for i in range(self.population_size):
            if ptr <= self.cumulative_distribution[i]:
                # print("...............selected = ", round(self.population[i].getTargetValue(), 2))
                return self.population[i]
        else:
            print("ERROR")

    def randomK(self, group_size=0.2):
        if (group_size % 1 != 0):
            group_size = int(floor(self.population_size * group_size))
        else:
            group_size = int(group_size)

        selected = []

        # TODO using random best fitted elems may be missed
        # TODO condition shuld be handled by fit method depending on type param
        selected = random.sample(self.population, group_size)  # sample - not repeats elems or choises - repeats elems
        best = min(selected, key=lambda ch: ch.getTargetValue())

        # return best
        return selected

    def tournament(self, group_size=0.2):
        if (group_size % 1 != 0):
            group_size = floor(self.population_size * group_size)
        else:
            group_size = int(group_size)

        selected = []

        for i in range(self.population_size):
            curr = self.population[i]
            if (i % group_size == 0):
                best = curr

            elif best.getTargetValue() > curr.getTargetValue() :
                best = curr

            if i % group_size == group_size - 1 or i == self.population_size - 1:
                selected.append(best)

        # print("I population : size : ", len(self.population), ' ', [round(x.getTargetValue(), 2) for x in self.population])
        # print("II selected : size : ", len(selected), ' ', [round(x.getTargetValue(), 2) for x in selected])

        # best = selected[random.randrange(0, len(selected), 1)]

        # return random.choice(selected)
        return selected

    def select(self, selection, parameter, parents):
        if selection == self.roulette:
            return Chromosome.constructFromParent(self.roulette())
        elif selection == self.randomK:
            return Chromosome.constructFromParent(min(self.randomK(parameter), key=lambda ch: ch.getTargetValue()))
        else:
            return Chromosome.constructFromParent(random.choice(parents))


