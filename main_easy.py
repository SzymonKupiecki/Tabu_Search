import random

import numpy as np
from matplotlib import pyplot as plt

from dtypes import ProblemInfo
from main_loop import optimize
from solution import Solution
from solution_matrix import sample_matrix_generator

# hard_matrix = np.array(np.mat("0 2 3 5; 5 0 7 3; 1 3 0 6; 1 4 8 0"))
#
# cable_vector = np.array(np.mat("2 5; 5 6; 4 5"))
#
# cost_tuples = np.array(np.mat("0 0 0; 2 3 4; 6 7 8; 7 4 5"))

def fun(hard_matrix_2, cable_vector_2, cost_tuples_2):
    info = ProblemInfo(hard_matrix_2, cable_vector_2, cost_tuples_2)

    starting_solution = Solution(sample_matrix_generator(0, len(info.hard_matrix), 3, 0.3), info)
    random.seed(None)
    res, his, change_his = optimize(starting_solution, info, tabu_length=20, midterm_memory=40, iterations=500, raport=True)

    return res
