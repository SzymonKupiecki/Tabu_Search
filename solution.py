import numpy as np
from quality import quality
from dtypes import ProblemInfo, ChangeType
from copy import deepcopy
from typing import List, Tuple
from solution_matrix import is_valid, matrix2adj
import random


class Solution:
    def __init__(self, matrix: np.ndarray, info: ProblemInfo, changes: List[Tuple[int, int, ChangeType]] = None):
        self.matrix_ = matrix
        self.quality_ = quality(info, matrix)
        if changes is None:
            self.changes_ = []
        else:
            self.changes_ = changes

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


def forbidden_moves(solution: Solution):
    # function return moves that should be forbidden - moves opposite to already made
    moves = []
    for change in solution.changes_:
        i, j, change_type = change
        match change_type:
            case ChangeType.INCREASE:
                moves.append((i, j, ChangeType.DECREASE))
            case ChangeType.DECREASE:
                moves.append((i, j, ChangeType.INCREASE))
            case ChangeType.ADDITION:
                moves.append((i, j, ChangeType.DELETION))
            case ChangeType.DELETION:
                moves.append((i, j, ChangeType.ADDITION))
    return moves


def find_neighbour_transfer(solution: Solution, info: ProblemInfo):
    # # FUNKCJA POWINNA TYLKO ZWIĘKSZAĆ I ZMNIEJSZAĆ PRZESYŁ NA ISTNIEJĄCYCH POŁĄCZENIACH
    # position = [0, 0]
    # matrix = deepcopy(solution.matrix_)
    # position[0] = np.random.randint(0, len(matrix)-1)
    # position[1] = np.random.randint(position[0]+1, len(matrix))
    # id_of_cable = np.random.randint(0, len(info.cable_vector))
    # increase_of_cable = np.random.randint(1, 5)
    # if np.random.randint(0, 2) == 1 or matrix[position[0]][position[1]][id_of_cable] < increase_of_cable:
    #     matrix[position[0]][position[1]][id_of_cable] += increase_of_cable
    # else:
    #     matrix[position[0]][position[1]][id_of_cable] -= increase_of_cable
    matrix = deepcopy(solution.matrix_)
    increase_of_cable = np.random.randint(1, 5)
    coords = np.argwhere(matrix != 0)
    coords = random.choice(coords)
    i = coords[0]
    j = coords[1]
    id_of_cable = np.random.randint(0, len(info.cable_vector))
    if np.random.randint(0, 2) == 1 or matrix[i][j][id_of_cable] < increase_of_cable:
        matrix[i][j][id_of_cable] += increase_of_cable
        matrix = Solution(matrix, info, changes=[(i, j, ChangeType.INCREASE)])
    else:
        matrix[i][j][id_of_cable] -= increase_of_cable
        if np.all(matrix[i][j] == 0):
            matrix = Solution(matrix, info, changes=[(i, j, ChangeType.DELETION), (i, j, ChangeType.DECREASE)])
        else:
            matrix = Solution(matrix, info, changes=[(i, j, ChangeType.DECREASE)])
    return matrix


def find_neighbour_connection(solution: Solution, info: ProblemInfo):
    # FUNKCJA POWINNA USUWAĆ ALBO DODAWAĆ Z POŁĄCZENIA Z ZACHOWANIEM ACYKLICZNOŚCI
    count = 0
    adj_matrix, _ = matrix2adj(solution.matrix_)
    while count < 50:
        try_matrix = deepcopy(solution.matrix_)
        coords = np.triu(np.argwhere(adj_matrix == 0))
        coords = random.choice(coords)
        i = coords[0]
        j = coords[1]
        if i >= j:
            count += 1
            continue
        try_matrix[i][j][0] = 3
        try_matrix[i][j][1] = 3
        try_matrix[i][j][2] = 3
        if is_valid(try_matrix):
            return Solution(try_matrix, info, changes=[(i, j, ChangeType.ADDITION)])
        count += 1
    return None
