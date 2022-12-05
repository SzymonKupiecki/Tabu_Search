
import numpy as np

class matrix_to_solve: # zmien nazwe
    def __init__(self, hard_matrix: np.ndarray[np.ndarray[int]], cable_vector: np.ndarray[(float, float)], cost_tuple: tuple):
        self.num_of_buildings = len(hard_matrix) # liczba budynków
        self.cable_vector =  cable_vector # [(koszt kabla, przesył)]
        self.cost_tuple = cost_tuple # (nr_budynku, żądany przesył, zysk, kara),  stworzyć liste indeks = nr budynku
        self.hard_matrix = hard_matrix # macierz trudności
        self.connection_matrix = [[[None for i in range(3)] for j in range(len(hard_matrix))] for k in range(len(hard_matrix))]

    def show_matrix(self, matrix):
        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()

    def insert_connection(self, num_row, num_col):
        if num_row != num_col:
            if num_row > num_col:
                num_row, num_col = num_col, num_row
            for i in range(3):
                self.connection_matrix[num_row][num_col][i] = 0
        else:
            print("Nie można łączyć tych samych budynków")
