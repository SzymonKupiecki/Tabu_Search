import random
import numpy as np
from dtypes import ProblemInfo, ChangeType
from main_loop import optimize
from solution_matrix import sample_matrix_generator
from solution import Solution
from matplotlib import pyplot as plt
import time



hard_matrix_wall_problem = [[0, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
                            [10000, 0, 2, 12, 14, 12, 13, 12, 26, 12, 8, 28],
                            [10000, 2, 0, 7, 12, 16, 12, 12, 3, 11, 23, 12],
                            [10000, 12, 7, 0, 23, 11, 12, 12, 23, 12, 8, 13],
                            [10000, 14, 12, 23, 0, 12, 13, 22, 6, 23, 12, 11],
                            [10000, 12, 16, 11, 12, 0, 12, 23, 11, 2, 4, 11],
                            [10000, 13, 12, 12, 13, 12, 0, 23, 12, 6, 4, 12],
                            [10000, 12, 12, 12, 22, 23, 23, 0, 12, 11, 2, 12],
                            [10000, 26, 3, 23, 6, 11, 12, 12, 0, 12, 4, 11],
                            [10000, 12, 11, 12, 23, 2, 6, 11, 12, 0, 12, 15],
                            [10000, 8, 23, 8, 12, 4, 4, 2, 4, 12, 0, 4],
                            [10000, 28, 12, 13, 11, 11, 12, 12, 11, 15, 4, 0]]

cable_vector_wall_problem = [(0.5, 20), (1, 48), (1.5, 76)]
cost_tuples_wall_problem = [(0, 0, 0), (50, 20000, 1000), (20, 10000, 750), (60, 25000, 2200), (120, 13000, 700),
                            (40, 11000, 700), (110, 10000, 950), (30, 30000, 2500), (110, 25000, 2300),
                            (70, 10000, 400), (20, 12000, 1100), (10, 11000, 1000)]

random.seed(2137)
hard_matrix_big_problem = [[0 if i == j else random.randint(10, 50) for i in range(30)] for j in range(30)]
cable_vector_big_problem = [(0.2, 20), (0.3, 35), (0.5, 60)]
cost_tuples_big_problem = [(0, 0, 0) if i == 0 else (random.randint(1, 10)*10, random.randint(1, 10)*100,
                                                     random.randint(1, 10)*50) for i in range(30)]

hard_matrix_time_problem = [[0 if i == j else random.randint(10, 50) for i in range(40)] for j in range(40)]
cable_vector_time_problem = [(0.2, 20), (0.3, 35), (0.5, 60)]
cost_tuples_time_problem = [(0, 0, 0) if i == 0 else (random.randint(1, 10)*10, random.randint(1, 10)*100,
                                                     random.randint(1, 10)*50) for i in range(40)]

info = ProblemInfo(
    np.array(hard_matrix_time_problem), np.array(cable_vector_time_problem), np.array(cost_tuples_time_problem))

starting_solution = Solution(sample_matrix_generator(0, len(info.hard_matrix), 3, 0.3), info)
random.seed(None)
start = time.time()
res, his, change_his = optimize(starting_solution, info, tabu_length=10, intermediate_term_memory=50, iterations=100,
                                raport=True, multiple_deletions=-1, number_of_neighbours_in_iteration=20)
end = time.time()
plt.plot(np.arange(0, len(his)), his)
plt.show()
chng_to_str = []
for elem in change_his:
    match elem[0][2]:
        case ChangeType.INCREASE:
            chng_to_str.append(1)
        case ChangeType.DECREASE:
            chng_to_str.append(2)
        case ChangeType.DELETION:
            chng_to_str.append(3)
        case ChangeType.ADDITION:
            chng_to_str.append(4)

his_to_file = str(his)
changes_in_str = str(chng_to_str)

with open("historyS1.txt", "w") as f_file:
    f_file.write(his_to_file)

with open("resultS_1.txt", "w") as f_file:
    f_file.write(str(res))

with open("resultS_2.txt", "w") as f_file:
    f_file.write(changes_in_str)

print(f"elapsed {end-start}")
