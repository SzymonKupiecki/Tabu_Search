
import numpy as np
from Szymon import Solution

class matrix_to_solve: # zmien nazwe
    # byl jakis blad w typyingu
    #def __init__(self, hard_matrix: np.ndarray[np.ndarray[int]], cable_vector: np.ndarray[(float, float)], cost_tuple: tuple):
    def __init__(self, hard_matrix, cable_vector, cost_tuple):
        self.num_of_buildings = len(hard_matrix)  # liczba budynków
        self.cable_vector = cable_vector  # [(koszt kabla, przesył)]
        self.cost_tuple = cost_tuple  # (żądany przesył, zysk, kara), indeks = nr budynku
        self.hard_matrix = hard_matrix  # macierz trudności

    # def show_matrix(self, matrix):
    #     for row in matrix:
    #         for val in row:
    #             print(val, end=" ")
    #         print()


# class Solution:
#     def __init__(self, matrix: np.ndarray, info: matrix_to_solve):
#         self.matrix_ = matrix
#         self.quality_ = quality(info, matrix)
#
#     def __eq__(self, other):
#         if isinstance(other, Solution):
#             if self.quality_ != other.quality_:
#                 return False
#             else:
#                 return np.all(self.matrix_ == other.matrix_)
#         elif isinstance(other, np.ndarray):
#             return np.all(self.matrix_ == other)
#
#     def __str__(self):
#         obj_str = ""
#         for row in self.matrix_:
#             for col in row:
#                 obj_str += np.array2string(col) + " "
#             obj_str += '\n'
#         return obj_str

class Tabu_list:
    def __init__(self, size):
        self.size = size
        self.tab = np.zeros((5,), dtype = int)

    def is_elem_in_tab(self, elem):
        for i in range(len(self.tab)):
            if elem == self.tab[i]:
                return True
        return False

    def get_elem(self):
        if self.tab != 0:
            return self.tab[0]
        else:
            return None

    def get_by_index(self, index):
        if index < len(self.tab):
            return self.tab[index]
        else:
            return None

    def insert_elem(self, elem):
        if isinstance(elem, Solution):
            for i in range(len(self.tab)): ## sprawdzam czy jest jakiś elem = 0 żeby go nadpisać
                if self.tab[i] == 0:
                    self.tab[i] = elem
                    return True
            self.tab = np.roll(self.tab, 1)
            self.tab[0] = elem
            self.tab = np.roll(self.tab,-1)
            return True
        else:
            return False