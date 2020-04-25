from src.gui import ga_gui
from src.logic.Target_function import function
from src.logic.Optimizer import Optimizer

class Tester:
    def __init__(self):
        self.environment_config_use_cases = []
        self.optimization_config_use_cases = []
        # self.optimizer = None
        # self.metrics = None

    def createEnvConfigUseCase(self):
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 10, 10, 0, False, 0.001]) # 0
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 10, 20, 0, False, 0.001]) # 1
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 10, 100, 0, False, 0.001]) # 3
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 20, 10, 0, False, 0.001]) # 4
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 20, 20, 0, False, 0.001]) # 5
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 20, 100, 0, False, 0.001]) # 6
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 100, 10, 0, False, 0.001]) # 7
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 100, 20, 0, False, 0.001]) # 8
        self.environment_config_use_cases.append([function, 2, (-1.5,4), (-3,4), 6, 100, 100, 0, False, 0.001]) # 9

    def createOptimConfigUseCase(self):
        # truncation, no elitism, mutation edge
        self.optimization_config_use_cases.append([('truncation', 0.25), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('united', 0.7), ('edge', 1, 0.1), 0.05, 0, None])

        # truncation, no elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('truncation', 0.25), ('onepoint', 0.7), ('any', 3,  0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('united', 0.7), ('any', 3, 0.1), 0.05, 0, None])

        # truncation, elitism, mutation edge
        self.optimization_config_use_cases.append([('truncation', 0.25), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('united', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])

        # truncation, elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('truncation', 0.25), ('onepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('truncation', 0.25), ('united', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])

        # tournament, no elitism, mutation edge
        self.optimization_config_use_cases.append([('tournament', 0.25), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('united', 0.7), ('edge', 1, 0.1), 0.05, 0, None])

        # tournament, no elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('tournament', 0.25), ('onepoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('united', 0.7), ('any', 3, 0.1), 0.05, 0, None])

        # tournament, elitism, mutation edge
        self.optimization_config_use_cases.append([('tournament', 0.25), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('united', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])

        # tournament, elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('tournament', 0.25), ('onepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('tournament', 0.25), ('united', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])

        # roulette, no elitism, mutation edge
        self.optimization_config_use_cases.append([('roulette', None), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('united', 0.7), ('edge', 1, 0.1), 0.05, 0, None])

        # roulette, no elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('roulette', None), ('onepoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 0, None])
        self.optimization_config_use_cases.append([('roulette', None), ('united', 0.7), ('any', 3, 0.1), 0.05, 0, None])

        # roulette, elitism, mutation edge
        self.optimization_config_use_cases.append([('roulette', None), ('onepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('twopoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('threepoint', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('united', 0.7), ('edge', 1, 0.1), 0.05, 1, 0.1])

        # roulette, elitism, mutation any 3-point
        self.optimization_config_use_cases.append([('roulette', None), ('onepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('twopoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('threepoint', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])
        self.optimization_config_use_cases.append([('roulette', None), ('united', 0.7), ('any', 3, 0.1), 0.05, 1, 0.1])

    def optConfUseCaseDecomposition(self, index):
        use_case = []
        for uc in self.optimization_config_use_cases[index]:
            if type(uc) is tuple or type(uc) is list:
                for el in uc:
                    use_case.append(el)
            else:
                use_case.append(uc)
        return use_case

    def envConfUseCaseDecomposition(self, index):
        use_case = []
        for uc in self.environment_config_use_cases[index]:
            if type(uc) is tuple or type(uc) is list:
                for el in uc:
                    use_case.append(el)
            else:
                use_case.append(uc)
        return use_case

    def run(self):
        if len(self.environment_config_use_cases) == 0:
            self.createEnvConfigUseCase()
        if len(self.optimization_config_use_cases) == 0:
            self.createOptimConfigUseCase()

        # RUN TESTS
        counter = 0
        env_counter = 0
        opt_counter = 0

        for env_cnf_use_case in self.environment_config_use_cases:
            opt_test = Optimizer(target=env_cnf_use_case[0],
                                 args_num=env_cnf_use_case[1],
                                 x1_range=env_cnf_use_case[2],
                                 x2_range=env_cnf_use_case[3],
                                 precision=env_cnf_use_case[4],
                                 epochs=env_cnf_use_case[5],
                                 population_size=env_cnf_use_case[6],
                                 type=env_cnf_use_case[7],
                                 plots=env_cnf_use_case[8],
                                 expected_accuracy=env_cnf_use_case[9])

            opt_counter = 0;
            for opt_cnf_use_case in self.optimization_config_use_cases:
                print("log : test : ", counter, " : env details : ", self.envConfUseCaseDecomposition(env_counter),
                      " : opt details : ", self.optConfUseCaseDecomposition(opt_counter))
                # optimizer.optimize(*opt_cnf_use_case)



                opt_test.optimize(selection=opt_cnf_use_case[0],
                                  crossover=opt_cnf_use_case[1],
                                  mutation=opt_cnf_use_case[2],
                                  inversion_prob=opt_cnf_use_case[3],
                                  elitism=opt_cnf_use_case[4],
                                  survival_rate=opt_cnf_use_case[5])

                print("best = ", opt_test.getBest().getTargetValue())
                print("time = ", sum(opt_test.computation_time))
                # opt_test.getMetrics()

                opt_test.reset()

                opt_counter += 1
                counter += 1

            env_counter += 1