import random
import numpy as np
from dtypes import ProblemInfo
from main_loop import optimize
from solution_matrix import sample_matrix_generator
from solution import Solution
from matplotlib import pyplot as plt
from examples import hard_matrix_1, cable_vector_1, cost_tuples_1
from examples import hard_matrix_2, cable_vector_2, cost_tuples_2
from examples import hard_matrix_3, cable_vector_3, cost_tuples_3
from examples import hard_matrix_4, cable_vector_4, cost_tuples_4

# sample data
hard_matrix = [[0, 20, 10, 15, 80, 60],
               [20,  0, 10, 40, 15, 10],
               [10, 10,  0,  5, 30, 20],
               [15, 40,  5,  0, 40, 25],
               [80, 15, 30, 40,  0, 5],
               [60, 10, 20,  25,  5, 0]]

cable_vector = [(0.15, 10), (0.25, 20), (0.5, 40)]

cost_tuples = [(0, 0, 0), (90, 300, 15), (110, 450, 70), (80, 150, 40), (70, 250, 20), (120, 100, 90)]

info = ProblemInfo(np.array(hard_matrix_2), np.array(cable_vector_2), np.array(cost_tuples_2))

starting_solution = Solution(sample_matrix_generator(0, len(info.hard_matrix), 3, 0.3), info)
random.seed(None)
res, his, change_his = optimize(starting_solution, info, tabu_length=100, iterations=500, raport=True)

plt.plot(np.arange(0, len(his)), his)
plt.show()
# plt.plot(np.arange(50, len(his)), his[50:])
# plt.show()
# plt.plot(np.arange(0, 30), his[0:30])
# plt.show()
his_to_file = str(his)

with open("history.txt", "w") as f_file:
    f_file.write(his_to_file)
