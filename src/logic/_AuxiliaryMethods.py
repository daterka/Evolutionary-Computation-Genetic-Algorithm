from datetime import datetime
import csv

from src.logic._Chromosome import Chromosome
from src.logic.configuration._Configuration import Config as cnf
def pickMoreAccurate(chromosome_1, chromosome_2, opt_type=0):
    if opt_type == 0:
        if chromosome_1.getTargetValue() <= chromosome_2.getTargetValue():
            return chromosome_1
        else:
            return chromosome_2
    else:
        if chromosome_1.getTargetValue() >= chromosome_2.getTargetValue():
            return chromosome_1
        else:
            return chromosome_2


def solutionError(solution_val):
    return abs(solution_val - cnf.y)

def exportToCSV(data = [], column_names = [], instane_info = ''):
    print('log : exporting results to csv')
    date_string = dateStr = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    filename = 'results/results_' + dateStr + '_' + instane_info + '.csv'

    with open(filename, mode='w', newline='') as results_csv:
        csv_writer = csv.writer(results_csv)
        csv_writer.writerow(column_names)
        csv_writer.writerows(data)

    results_csv.close()