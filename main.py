import random
import numpy as np
from dtypes import ProblemInfo
from main_loop import optimize
from solution_matrix import sample_matrix_generator
from solution import Solution
from matplotlib import pyplot as plt
import ast
from examples import hard_matrix_1, cable_vector_1, cost_tuples_1

def fun():
    with open("hard_matrix.txt", "r") as f_file1:
        hard_matrix = ast.literal_eval(f_file1.read())

    with open("cable_vector.txt", "r") as f_file2:
        cable_vector = ast.literal_eval(f_file2.read())
    for i in cable_vector:
        i = tuple(i)

    with open("cost_tuples.txt", "r") as f_file3:
        cost_tuples = ast.literal_eval(f_file3.read())
    for i in cost_tuples:
        i = tuple(i)

    with open("iteration.txt", "r") as f_file4:
        iteration = ast.literal_eval(f_file4.read())

    with open("mid_mem.txt", "r") as f_file5:
        mid_mem = ast.literal_eval(f_file5.read())

    with open("tabu.txt", "r") as f_file5:
        tabu = ast.literal_eval(f_file5.read())

    info = ProblemInfo(np.array(hard_matrix), np.array(cable_vector), np.array(cost_tuples))

    starting_solution = Solution(sample_matrix_generator(0, len(info.hard_matrix), 3, 0.3), info)
    random.seed(None)
    res, his, change_his = optimize(starting_solution, info, tabu_length=tabu, intermediate_term_memory=mid_mem, iterations=iteration, raport=True)

    plt.plot(np.arange(0, len(his)), his)
    plt.savefig('plot.png')
    plt.show()
    plt.savefig('plot_blank.png')
    # plt.plot(np.arange(50, len(his)), his[50:])
    # plt.show()
    # plt.plot(np.arange(0, 30), his[0:30])
    # plt.show()
    his_to_file = str(his)

    with open("history.txt", "w") as f_file:
        f_file.write(his_to_file)

    with open("res.txt", "w") as f_file:
        f_file.write(str(res))
