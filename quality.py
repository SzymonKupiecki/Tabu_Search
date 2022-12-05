from Szymon import sample_matrix_generator, Solution
import numpy as np

t = Solution(sample_matrix_generator(0, 8, 3))


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

def quality(matrix):
    adj_matrix, adj_list = matrix2adj(matrix)
    for neig

m, l = matrix2adj(t.matrix_)
print(l)
