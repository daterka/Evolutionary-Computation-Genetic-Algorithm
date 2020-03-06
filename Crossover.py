from Chromosome import Chromosome
import random

def cross_onepoint(chromosome1, chromosome2,chance = 1, value = -1):
    if random.random() > chance:
        return chromosome1,chromosome2
    else:
        if value < 0:
            value = random.randrange(chromosome1.chromosome_length)

        tmp1 = chromosome1.representation.copy()
        tmp2 = chromosome2.representation.copy()

        tmp1 = tmp1[:value]+chromosome2.representation[value:]
        tmp2 = tmp2[:value]+chromosome1.representation[value:]
        print ("Crossed")
        print (tmp1)
        print (tmp2)
        tmp1 = tmp1.copy()
        tmp2 = tmp2.copy()
        
        chromosome1.representation = tmp1
        chromosome2.representation = tmp2
        
        return chromosome1, chromosome2

def cross_twopoint(chromosome1, chromosome2,chance = 1, value = [-1,-1]):
    if random.random() > chance:
        return chromosome1,chromosome2
    else:
        if value[0] < 0 or value[1] < 0 or value[0]>value[1]:
            value = []
            value.append(random.randrange(chromosome1.chromosome_length-2))
            value.append(random.randrange(value[0]+1,chromosome1.chromosome_length))

        tmp1 = chromosome1.representation.copy()
        tmp2 = chromosome2.representation.copy()

        tmp1 = tmp1[:value[0]]+chromosome2.representation[value[0]:value[1]]+tmp1[value[1]:]
        tmp2 = tmp2[:value[0]]+chromosome1.representation[value[0]:value[1]]+tmp2[value[1]:]
        print ("Crossed points {}  {}".format(value[0],value[1]))
        print (tmp1)
        print (tmp2)
        
        tmp1 = tmp1.copy()
        tmp2 = tmp2.copy()

        chromosome1.representation = tmp1
        chromosome2.representation = tmp2
        
        return chromosome1, chromosome2

def cross_threepoint(chromosome1, chromosome2,chance = 1,  value = [-1,-1, -1]):
    if random.random() > chance:
        return chromosome1,chromosome2
    else:
        if value[0] < 0 or value[1] < 0 or value[2] < 0 or value[0]>value[1] or value[1]>value[2] :
            value = []
            value.append(random.randrange(chromosome1.chromosome_length-3))
            value.append(random.randrange(value[0]+1,chromosome1.chromosome_length-2))
            value.append(random.randrange(value[1]+1,chromosome1.chromosome_length))

        tmp1 = chromosome1.representation.copy()
        tmp2 = chromosome2.representation.copy()

        tmp1 = tmp1[:value[0]]+chromosome2.representation[value[0]:value[1]]+tmp1[value[1]:value[2]]+chromosome2.representation[value[2]:]
        tmp2 = tmp2[:value[0]]+chromosome1.representation[value[0]:value[1]]+tmp2[value[1]:value[2]]+chromosome1.representation[value[2]:]
        print ("Crossed points {}  {}  {}".format(value[0],value[1], value[2]))
        print (tmp1)
        print (tmp2)

        tmp1 = tmp1.copy()
        tmp2 = tmp2.copy()

        chromosome1.representation = tmp1
        chromosome2.representation = tmp2
        
        return chromosome1, chromosome2

def cross_united(chromosome1,chromosome2,chance = 1):
    if random.random() > chance:
        return chromosome1,chromosome2
    else:
        tmp1 = []
        tmp2 = []
        for i,j in zip(chromosome1.representation,chromosome2.representation):
            if random.random() > 0.5:
                tmp1.append(i)
                tmp2.append(j)
            else:
                tmp1.append(j)
                tmp2.append(i)
        tmp1 = tmp1.copy()
        tmp2 = tmp2.copy()

        chromosome1.representation = tmp1
        chromosome2.representation = tmp2

        return chromosome1, chromosome2


