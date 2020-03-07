import random


class Chromosome:

    def __init__(self, chromosome_length = 10):
        self.representation = [random.randrange(2) for x in range(chromosome_length)]
        self.chromosome_length = chromosome_length
    def __repr__(self):
        return repr(self.representation)
