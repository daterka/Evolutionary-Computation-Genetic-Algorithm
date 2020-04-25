from src.logic._Chromosome import Chromosome
import random

class Crossover:
    def cross_onepoint(self, chromosome1, chromosome2, chance=1, value=-1):
        if random.random() > chance:
            return Chromosome.constructFromParent(chromosome1), Chromosome.constructFromParent(chromosome2)
        else:
            if value < 0:
                value = random.randrange(chromosome1.chromosome_length)

            tmp1 = chromosome1.representation.copy()
            tmp2 = chromosome2.representation.copy()

            tmp1 = tmp1[:value] + chromosome2.representation[value:]
            tmp2 = tmp2[:value] + chromosome1.representation[value:]

            tmp1 = tmp1.copy()
            tmp2 = tmp2.copy()

            # chromosome1.representation = tmp1
            # chromosome2.representation = tmp2
            newChromosome1 = Chromosome(tmp1)
            newChromosome2 = Chromosome(tmp2)

            return newChromosome1, newChromosome2

    def cross_twopoint(self, chromosome1, chromosome2, chance=1, value=[-1, -1]):
        if random.random() > chance:
            return Chromosome.constructFromParent(chromosome1), Chromosome.constructFromParent(chromosome2)
        else:
            if value[0] < 0 or value[1] < 0 or value[0] > value[1]:
                value = []
                value.append(random.randrange(chromosome1.chromosome_length - 2))
                value.append(random.randrange(value[0] + 1, chromosome1.chromosome_length))

            tmp1 = chromosome1.representation.copy()
            tmp2 = chromosome2.representation.copy()

            tmp1 = tmp1[:value[0]] + chromosome2.representation[value[0]:value[1]] + tmp1[value[1]:]
            tmp2 = tmp2[:value[0]] + chromosome1.representation[value[0]:value[1]] + tmp2[value[1]:]

            tmp1 = tmp1.copy()
            tmp2 = tmp2.copy()

            # chromosome1.representation = tmp1
            # chromosome2.representation = tmp2
            newChromosome1 = Chromosome(tmp1)
            newChromosome2 = Chromosome(tmp2)

            return newChromosome1, newChromosome2

    def cross_threepoint(self, chromosome1, chromosome2, chance=1, value=[-1, -1, -1]):
        if random.random() > chance:
            return Chromosome.constructFromParent(chromosome1), Chromosome.constructFromParent(chromosome2)
        else:
            if value[0] < 0 or value[1] < 0 or value[2] < 0 or value[0] > value[1] or value[1] > value[2]:
                value = []
                value.append(random.randrange(chromosome1.chromosome_length - 3))
                value.append(random.randrange(value[0] + 1, chromosome1.chromosome_length - 2))
                value.append(random.randrange(value[1] + 1, chromosome1.chromosome_length))

            tmp1 = chromosome1.representation.copy()
            tmp2 = chromosome2.representation.copy()

            tmp1 = tmp1[:value[0]] + chromosome2.representation[value[0]:value[1]] + tmp1[value[1]:value[
                2]] + chromosome2.representation[value[2]:]
            tmp2 = tmp2[:value[0]] + chromosome1.representation[value[0]:value[1]] + tmp2[value[1]:value[
                2]] + chromosome1.representation[value[2]:]

            tmp1 = tmp1.copy()
            tmp2 = tmp2.copy()

            # chromosome1.representation = tmp1
            # chromosome2.representation = tmp2
            newChromosome1 = Chromosome(tmp1)
            newChromosome2 = Chromosome(tmp2)

            return newChromosome1, newChromosome2

    def cross_united(self, chromosome1, chromosome2, chance=1):
        if random.random() > chance:
            return Chromosome.constructFromParent(chromosome1), Chromosome.constructFromParent(chromosome2)
        else:
            tmp1 = []
            tmp2 = []
            for i, j in zip(chromosome1.representation, chromosome2.representation):
                if random.random() > 0.5:
                    tmp1.append(i)
                    tmp2.append(j)
                else:
                    tmp1.append(j)
                    tmp2.append(i)
            tmp1 = tmp1.copy()
            tmp2 = tmp2.copy()

            # chromosome1.representation = tmp1
            # chromosome2.representation = tmp2
            newChromosome1 = Chromosome(tmp1)
            newChromosome2 = Chromosome(tmp2)

            return newChromosome1, newChromosome2


