import numpy as np
import random


def is_cyclic_by_dfs(adj_list):
    visited = list()
    cycle_exists = False
    stack = [0]  # creating a stack
    while stack:
        v = stack.pop()
        if v not in visited:  # if vertex wasn't visited:
            visited.append(v)  # mark as visited
            no_of_neighbours_visited = 0
            for u in adj_list[v][::-1]:  # for every "u" in adj_lst of "v"
                stack.append(u)  # append "u" to stack
                if u in visited:  # if "u" is already visited
                    no_of_neighbours_visited += 1
                    if no_of_neighbours_visited > 1:
                        cycle_exists = True
                        return cycle_exists
    return cycle_exists


def is_valid(matrix: np.ndarray):
    size = len(matrix)
    # create adjacent matrix and list
    adj_matrix, adj_list = matrix2adj(matrix)
    # check horizontal connections
    for row in adj_matrix:
        if np.sum(row) > 3:
            return False
    # check vertical connections
    for i in range(size):
        if np.sum(adj_matrix[:, i]) > 3:
            return False
    # check if there is no cycles, if there are return false otherwise true
    return not is_cyclic_by_dfs(adj_list)

def matrix2adj(matrix):
    size = len(matrix)
    adj_matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if not np.all(matrix[i][j] == 0):
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1
    adj_list = {}
    for i, row in enumerate(adj_matrix):
        neighbors = []
        for j in range(size):
            if row[j] == 1:
                neighbors.append(j)
        adj_list[i] = neighbors
    return adj_matrix, adj_list


def sample_matrix_generator(seed, size, con_num=3, chance=0.5):
    matrix = None
    random.seed(seed)
    count = 0
    while True and count < 1000:
        matrix = np.zeros((size, size, con_num), dtype=int)
        adj_matrix = np.zeros((size, size), dtype=int)
        for row in range(size):
            for col in range(size):
                if row >= col:
                    continue
                else:
                    # ilość połączeń mniejsza niż 3
                    if np.sum(adj_matrix[row]) <= 3 and np.sum(adj_matrix[:, col]) <= 3:
                        if random.random() < chance:
                            adj_matrix[row][col] = 1
                            for i in range(con_num):
                                matrix[row][col][i] = random.randint(0, 5)
        if is_valid(matrix):
            break
        count += 1
    return matrix
