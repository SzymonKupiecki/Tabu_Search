
import numpy as np

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
