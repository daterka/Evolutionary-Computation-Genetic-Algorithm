import random


class Mutation:
    def mutate(self, chromosome, n, prob):
        r = random.random()
        if(r <= prob):

            for i in range(0, n, 1):
                indx = random.randrange(0, (chromosome.len()), 1)
                chromosome.representation[indx] = abs(chromosome.representation[indx]-1)


        return chromosome

    def mutateEdge(self, chromosome, n, prob):
        r = random.random()
        if(r <= prob):
            chromosome.representation[0] = abs(chromosome.representation[0]-1)

        r = random.random()
        if(n > 1 and r <= prob):
            indx = chromosome.len()-1
            chromosome.representation[indx] = abs(chromosome.representation[indx]-1)

        return chromosome