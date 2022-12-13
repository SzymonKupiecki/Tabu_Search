import numpy as np
from dtypes import matrix_to_solve
from Szymon import sample_matrix_generator, is_valid, optimize
from solution import Solution
from Jan import Tabu_list

# sample data
hard_matrix = [[0, 20, 10, 15, 80, 60],
               [20,  0, 10, 40, 15, 10],
               [10, 10,  0,  5, 30, 20],
               [15, 40,  5,  0, 40, 25],
               [80, 15, 30, 40,  0, 5],
               [60, 10, 20,  25,  5, 0]]

cable_vector = [(15, 10), (25, 20), (50, 40)]

cost_tuples = [(0, 0, 0), (90, 300, 15), (110, 450, 70), (80, 150, 40), (70, 250, 20), (120, 100, 90)]

info = matrix_to_solve(np.array(hard_matrix), np.array(cable_vector), np.array(cost_tuples))

starting_solution = sample_matrix_generator(0, 6, 3, 0.35)

valid_matrix = is_valid(starting_solution)
i = 1

while not valid_matrix and i < 10000:
    starting_solution = sample_matrix_generator(i, 6, 3, 0.35)
    i += 1
    valid_matrix = is_valid(starting_solution)

starting_solution = Solution(starting_solution, info)

# print(i)
# print(starting_solution)
# print(starting_solution.quality_)

# res = optimize(starting_solution, info)
# print(res.quality_)
# print(res)

test = Tabu_list(2)
test.insert_elem(starting_solution)