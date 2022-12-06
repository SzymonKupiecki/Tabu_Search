import numpy as np
import random


# placeholder
def quality(matrix):
    return np.sum(matrix)


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


def sample_matrix_generator(seed, size, con_num=3, chance=0.5):
    random.seed(seed)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            con = []
            for _ in range(con_num):
                individual_chance = random.random()
                if i >= j:
                    con.append(0)
                else:
                    if individual_chance < chance:
                        con.append(random.randint(0, 5))
                    else:
                        con.append(0)
            row.append(con)
        matrix.append(row)

    return np.array(matrix)


class Solution:
    def __init__(self, matrix: np.ndarray):
        self.matrix_ = matrix
        self.quality_ = quality(matrix)

    def __eq__(self, other):
        if isinstance(other, Solution):
            if self.quality_ != other.quality_:
                return False
            else:
                return np.all(self.matrix_ == other.matrix_)
        elif isinstance(other, np.ndarray):
            return np.all(self.matrix_ == other)

    def __str__(self):
        obj_str = ""
        for row in self.matrix_:
            for col in row:
                obj_str += np.array2string(col) + " "
            obj_str += '\n'
        return obj_str
