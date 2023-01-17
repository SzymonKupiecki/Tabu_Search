import numpy as np
from src.quality import quality
from src.dtypes import ProblemInfo, ChangeType
from copy import deepcopy
from typing import List, Tuple
from src.solution_matrix import is_valid, matrix2adj
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
    matrix = deepcopy(solution.matrix_)
    increase_of_cable = np.random.randint(1, 5)
    coords = np.argwhere(matrix != 0)
    if len(coords) < 1:
        return None
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


def find_neighbour_add_connection(solution: Solution, info: ProblemInfo):
    count = 0
    adj_matrix, _ = matrix2adj(solution.matrix_)
    adj_matrix = np.triu(adj_matrix)
    coords = np.argwhere(adj_matrix == 0)
    while count < 30:
        try_matrix = deepcopy(solution.matrix_)
        chosen_coords = random.choice(coords)
        i = chosen_coords[0]
        j = chosen_coords[1]
        if i >= j:
            count += 1
            continue
        for z in range(len(try_matrix[i][j])):
            try_matrix[i][j][z] = random.randint(0, 5)
        if is_valid(try_matrix):
            return Solution(try_matrix, info, changes=[(i, j, ChangeType.ADDITION)])
        count += 1
    return None


def find_neighbour_del_connection(solution: Solution, info: ProblemInfo, number_of_connections):
    adj_matrix, _ = matrix2adj(solution.matrix_)
    adj_matrix = np.triu(adj_matrix)
    coords = np.argwhere(adj_matrix != 0)
    corrected_number_of_connections = min(number_of_connections, len(coords))
    coords_lst_idx = random.sample(list(range(len(coords))), corrected_number_of_connections)
    try_matrix = deepcopy(solution.matrix_)
    changes_lst = []
    for act_coords_idx in coords_lst_idx:
        coords_chosen = coords[act_coords_idx]
        i = coords_chosen[0]
        j = coords_chosen[1]
        for z in range(len(try_matrix[i][j])):
            try_matrix[i][j][z] = 0
        changes_lst.append((i, j, ChangeType.DELETION))
    return Solution(try_matrix, info, changes=changes_lst)
