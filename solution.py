import numpy as np
from quality import quality
from dtypes import ProblemInfo
from copy import deepcopy


class Solution:
    def __init__(self, matrix: np.ndarray, info: ProblemInfo):
        self.matrix_ = matrix
        self.quality_ = quality(info, matrix)

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
        obj_str += f"Quality = {self.quality_}"
        return obj_str


def find_neighbour(solution: np.ndarray, info: ProblemInfo):
    position = [0, 0]
    matrix = deepcopy(solution)
    position[0] = np.random.randint(0, len(matrix)-1)
    position[1] = np.random.randint(position[0]+1, len(matrix))
    id_of_cable = np.random.randint(0, len(info.cable_vector))
    increase_of_cable = np.random.randint(1, 5)
    if np.random.randint(0, 2) == 1 or matrix[position[0]][position[1]][id_of_cable] < increase_of_cable:
        matrix[position[0]][position[1]][id_of_cable] += increase_of_cable
    else:
        matrix[position[0]][position[1]][id_of_cable] -= increase_of_cable
    return matrix
