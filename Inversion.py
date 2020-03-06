from Chromosome import Chromosome
import random

def inversion(chromosome1,chance = 1, value = [-1,-1]):
    if random.random() > chance:
        return chromosome1
    else:
        if value[0] < 0 or value[1] < 0 or value[0]>value[1]:
            value = []
            value.append(random.randrange(chromosome1.chromosome_length-2))
            value.append(random.randrange(value[0]+1,chromosome1.chromosome_length))

        tmp1 = chromosome1.representation.copy()
        sliced = chromosome1.representation[value[0]:value[1]]
        inverted = []
        for i in sliced:
            inverted.append(abs(i-1))

        tmp1 = tmp1[:value[0]]+inverted+tmp1[value[1]:]
        print ("Crossed points {}  {}".format(value[0],value[1]))
        print (tmp1)
        
        tmp1 = tmp1.copy()

        chromosome1.representation = tmp1
        
        return chromosome1


c1 = Chromosome()

print(c1)

print(inversion(c1))
