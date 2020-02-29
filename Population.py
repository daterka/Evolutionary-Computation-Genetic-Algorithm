from Chromosome import Chromosome


class Population:
    def __init__(self, pop_length=5, chromosome_length=10):
        self.population = [Chromosome(chromosome_length) for x in range(pop_length)]

    def __repr__(self):
        return repr(self.population)
