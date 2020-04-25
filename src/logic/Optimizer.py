from src.logic.configuration._Configuration import Config as cnf
from src.logic._Chromosome import Chromosome
from src.logic.selection._Selection import Selection
from src.logic.operators._Crossover import Crossover
from src.logic.operators._Inversion import Inversion
from src.logic.operators._Mutation import Mutation
from math import ceil, floor, log2, sqrt
import random
from src.logic import plots
from timeit import default_timer as timer
from src.logic._AuxiliaryMethods import *

# Module scopes
class Optimizer(cnf, Selection, Crossover, Inversion, Mutation):
    def __init__(self, epochs=10, population_size=10, target=None, precision=6, type=0,
                 args_num=2, x1_range=(-1, 1), x2_range=(-1, 1), plots = True, expected_accuracy=0.001):
        print("log : Initiation on new optimizer Instance")
        cnf.epochs = epochs
        cnf.population_size = population_size
        cnf.target = target
        cnf.args_num = args_num
        cnf.precision = precision
        cnf.type = type
        cnf.x1_a, cnf.x1_b = x1_range
        cnf.x2_a, cnf.x2_b = x2_range
        cnf.x1_length = self.argLength(abs(self.x1_b - self.x1_a))
        cnf.x2_length = self.argLength(abs(self.x2_b - self.x2_a))
        cnf.chromosome_length = self.x1_length + self.x2_length
        self.plots = plots
        self.expected_accuracy = expected_accuracy

        self.instance_info = '_epochs_'+str(epochs)+'_popSize_'+str(population_size)

        self.population = None
        self.computation_time = []
        self.best_chrom_per_epoch = []
        self.mean_per_epoch = []
        self.variance_per_erpoch = []
        self.standard_deviation_per_epoch = []
        self.mae_per_epoch = []

        self.current_best = []

    # TODO handling custom numbers of agrs

    def argLength(self, domain_len):
        return (ceil(log2(domain_len * pow(10, self.precision)) + log2(1)))

    def chromosomeLength(self):
        x1_length = self.argLength(abs(self.x1_b - self.x1_a))
        x2_length = self.argLength(abs(self.x2_b - self.x2_a))
        return x1_length + x2_length



    def initPopulation(self):
        # TODO make more readable
        print('log : Initiation a new population ')
        self.population = [Chromosome([random.randrange(2) for x in range(self.chromosome_length)], self.chromosome_length) for x in
                           range(self.population_size)]

        self.current_best = [self.population[0], -1, -1, -1, -1, -1]

    # TODO format
    def evaluate(self):
        i = 0
        best = (self.population[0] if self.population != None else None)
        # best.setTargetValue(best.decode())
        sum = 0
        sqrt_sum = 0
        sum_mae = 0
        for chromosome in self.population:
            # target_val = cnf.target(chromosome.decode())
            target_val = chromosome.getTargetValue()
            # chromosome.setTargetValue(target_val)
            if target_val < best.getTargetValue():
                best = chromosome
                # print("index = ", i, ' best = ', best.getTargetValue())
            i+=1

            sum += target_val
            sqrt_sum += target_val*target_val

            sum_mae += abs(cnf.y-target_val)


        # print("I ******** population : size : ", len(self.population), ' ' , [round(x.getTargetValue(), 2) for x in self.population])
        mean = sum/self.population_size

        variance = (sqrt_sum-(sum*sum)/self.population_size)/self.population_size
        if variance <= 0:
            std = 0
        else:
            std = sqrt(variance)

        mae = sum_mae/self.population_size
        self.best_chrom_per_epoch.append(best)
        self.mean_per_epoch.append(mean)
        self.variance_per_erpoch.append(variance)
        self.standard_deviation_per_epoch.append(std)
        self.mae_per_epoch.append(mae)

        # self.current_best = pickMoreAccurate(self.current_best, best, cnf.type)

        # print("\nI .....log : evaluation : best=", round(best.getTargetValue(),2), ", mean=", round(mean,2), ", variance=", round(variance,2), ", std=", round(std,2))

        return [best, mean, variance, std, mae]
    # TODO todo..
    def validateChromosome(self):
        pass

    # TODO mote suitable method name
    def reproduction(self):
        offspring = []

        selected_candidates = None
        if cnf.selection == self.roulette:
            self.normalizePopulation()
        elif cnf.selection == self.truncation or cnf.selection == self.tournament:
            selected_candidates = cnf.selection(cnf.selection_parameter)

        if cnf.elitism == 1:
            # number of fittest parents to be preserved to next gen
            if cnf.survival_rate % 1 != 0:
                survival_n = floor(self.population_size * cnf.survival_rate)
            else:
                survival_n = int(cnf.survival_rate)

            offspring_n = self.population_size - survival_n

            offspring = self.truncation(survival_n)

        # TODO indexes of population, try less computationally complex, out of range
        while len(offspring) <= self.population_size: # < enough??
            # TODO make selection return new chromosome, not exact objects from population !

            parent_1 = self.select(cnf.selection, cnf.selection_parameter, selected_candidates)
            parent_2 = self.select(cnf.selection, cnf.selection_parameter, selected_candidates)

            child_1, child_2 = cnf.crossover(parent_1, parent_2, cnf.crossover_prob)

            child_1 = cnf.mutation(child_1, cnf.mutation_n, cnf.mutation_prob)
            child_2 = cnf.mutation(child_2, cnf.mutation_n, cnf.mutation_prob)

            child_1 = self.invert(child_1, cnf.inversion_prob)
            child_2 = self.invert(child_2, cnf.inversion_prob)
            # TODO inlude both childs or just best or check if better than parents ??
            offspring.append(child_1)
            offspring.append(child_2)

        return offspring[:self.population_size]

    def nextGen(self):
        # TODO add exceptions if not enough params provided
        self.population = self.reproduction()

    def getBest(self):
        best_solution_found = {
            'chromosome' : self.current_best[0],
            'mean' : self.current_best[1],
            'variance' : self.current_best[2],
            'std' : self.current_best[3],
            'mae' : self.current_best[4],
            'time' : self.current_best[5],
            'epoch' : self.current_best[6]
        }
        print(best_solution_found)
        return best_solution_found

    def resultsToCsv(self):
        data = zip(
            [x.decode() for x in self.best_chrom_per_epoch],
            [x.getTargetValue() for x in self.best_chrom_per_epoch],
            self.mean_per_epoch,
            self.variance_per_erpoch,
            self.standard_deviation_per_epoch,
            self.mae_per_epoch,
            self.computation_time
        )
        names = ['(x1, x2)', 'y', 'mean', 'variance', 'std', 'mae', 'time']
        exportToCSV(data, names, self.instance_info)

    def run(self):
        # GA algorithm
        # if (self.population is None):
        #     self.initPopulation()
        start = timer()
        self.initPopulation()
        current_result = self.evaluate()  # move into while
        duration = timer() - start
        current_result.append(duration)
        epochs_counter = 0
        while (epochs_counter < self.epochs):
            print("log : Starting New Epoch no. counter ", epochs_counter)
            start = timer()
            self.nextGen()
            duration += timer() - start
            current_result = self.evaluate()

            if self.current_best[0].getTargetValue() > current_result[0].getTargetValue():
                current_result.append(duration)
                current_result.append(epochs_counter)
                self.current_best = current_result

            self.computation_time.append(duration)

            if solutionError(self.current_best[0].getTargetValue()) < self.expected_accuracy:
                print("log : process terminated due to expected accuracy being achieved in epoch : ", epochs_counter)
                break

            epochs_counter += 1

    def plotAll(self):
        print('log : plotting results..')
        plots.plotSimple([x.getTargetValue() for x in self.best_chrom_per_epoch], 'best_target_vals', 'epochs', 'best_target_vals_per_epoch', self.instance_info)
        plots.plotSimple(self.mean_per_epoch, 'mean', 'epochs', 'mean_per_epoch', self.instance_info)
        plots.plotSimple(self.variance_per_erpoch, 'variance', 'epochs', 'variance_per_epoch', self.instance_info)
        plots.plotSimple(self.standard_deviation_per_epoch, 'std', 'epochs', 'std_per_epoch', self.instance_info)
        plots.plotSimple(self.mae_per_epoch, 'mae', 'epochs', 'mae_per_epoch', self.instance_info)
        plots.plotSimple(self.computation_time, 'time', 'epochs', 'time_per_epoch', self.instance_info)


    def reset(self):
        self.cumulative_distribution = []
        self.instance_info = '_epochs_'+str(cnf.epochs)+'_popSize_'+str(cnf.population_size)

        self.population = None
        self.computation_time = []
        self.best_chrom_per_epoch = []
        self.mean_per_epoch = []
        self.variance_per_erpoch = []
        self.standard_deviation_per_epoch = []
        self.mae_per_epoch = []

        self.current_best = None

    def optimize(self, selection=("roulette", None),
                 crossover=("threepoint", 0.7),
                 mutation=("any", 3, 0.3),
                 inversion_prob = 0.05,
                 elitism = 1, survival_rate = 0.1):

        # optimization configuration
        # TODO seperate setting configuration outside
        cnf.elitism = elitism
        cnf.survival_rate = survival_rate
        cnf.inversion_prob = inversion_prob

        selection, cnf.selection_parameter = selection
        self.instance_info += '_'+selection
        if selection == "truncation" or selection == 0:
            cnf.selection = self.truncation
        elif selection == "tournament" or selection == 1:
            cnf.selection = self.tournament
        elif selection == "randomK" or selection == 2:
            cnf.selection = self.randomK
        else:
            cnf.selection = self.roulette



        crossover, cnf.crossover_prob = crossover
        self.instance_info += '_' + crossover
        if crossover == "onepoint" or crossover == 0:
            cnf.crossover = self.cross_onepoint
        elif crossover == "twopoint" or crossover == 1:
            cnf.crossover = self.cross_twopoint
        elif crossover == "threepoint"  or crossover == 2:
            cnf.crossover = self.cross_threepoint
        else:
            cnf.crossover = self.cross_united

        mutation, cnf.mutation_n, cnf.mutation_prob = mutation
        self.instance_info += '_' + mutation
        if mutation == "edge":
            cnf.mutation = self.mutateEdge
        else:
            cnf.mutation = self.mutate

        self.instance_info += '_' + 'elitism_'+str(elitism)

        self.run()

        if(self.plots):
            self.plotAll()

        plots.plotBestPerEpoch([x.getTargetValue() for x in self.best_chrom_per_epoch])
        self.resultsToCsv()

    def getMetrics(self):
        print("best : ", [round(x.getTargetValue(), 2) for x in self.best_chrom_per_epoch])
        print("time : ", [round(x, 5) for x in self.computation_time])
        print("mean : ", [round(x, 2) for x in self.mean_per_epoch])
        print("variance : ", [round(x, 2) for x in self.variance_per_erpoch])
        print("std : ", [round(x, 2) for x in self.standard_deviation_per_epoch])
        print("mae : ", [round(x, 2) for x in self.mae_per_epoch])

        return [self.computation_time, self.best_chrom_per_epoch, self.mean_per_epoch,
                self.variance_per_erpoch, self.standard_deviation_per_epoch,
                self.mae_per_epoch]

