import numpy as np
import random


# placeholder
def quality(matrix):
    return np.sum(matrix)


def sample_matrix_generator(seed, size, con_num):
    random.seed(seed)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            con = []
            for _ in range(con_num):
                if i >= j:
                    con.append(0)
                else:
                    con.append(random.randint(0, 5))
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
