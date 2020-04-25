from src.gui import ga_gui
from src.logic.Target_function import function
from src.logic.Optimizer import Optimizer
from src.test.tests import Tester

# Number of epochs, just a variable
EPOCHS = 100

# Number of individuals
POPULATION_SIZE = 20

# Target args number
N = 2
# Range of args
X1_RANGE = (-1.5, 4)
X2_RANGE = (-3, 4)

# Solution precision
PRECISION = 6

# Optimalization type
opt_type = 0 # minimalization

# selection
selection = "tournament"
selection_parameter = 3

# crossover
crossover = "threepoint"
crossover_prob = 0.9

# mutation
mutation = "any"
mutation_n = 3
mutation_prob = 0.1

# inversion
inversion_prob = 0.05

# elitism
elitism = True
survival_rate = 0.1


def test0():
    # TEST0
    opt_test = Optimizer(target=function, args_num=N, x1_range=X1_RANGE, x2_range=X2_RANGE,
                         precision=PRECISION, epochs=EPOCHS, population_size=POPULATION_SIZE, type=0)

    # opt_test.initPopulation()

    opt_test.optimize(selection=(selection, selection_parameter),
                      crossover=(crossover, crossover_prob),
                      mutation=(mutation, mutation_n, mutation_prob),
                      inversion_prob=inversion_prob,
                      elitism=elitism, survival_rate=survival_rate)

    best = opt_test.getBest()
    print("found solution : best : ", best.get('chromosome').decode(), best.get('chromosome').getTargetValue(),
          'mean : ', best.get('mean'), ' variance : ', best.get('variance'), ' std : ', best.get('std'),
          ' mae : ', best.get('mae'), ' time : ', best.get('time'), ' epoch : ', best.get('epoch'))

    opt_test.getMetrics()




def gui():
    ga_gui.vp_start_gui()

def main():
    gui()
    # test0()
    # tester = Tester()
    # tester.run()

main()
