import numpy as np
import random
from quality import matrix2adj, find_neighbour
from dtypes import ProblemInfo
from solution import Solution
from Jan import TabuList


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


def sample_matrix_generator(seed, size, con_num=3, chance=0.5):
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
                        if random.random() > chance:
                            adj_matrix[row][col] = 1
                            for i in range(con_num):
                                matrix[row][col][i] = random.randint(0, 5)
        if is_valid(matrix):
            break
        count += 1
    return matrix


def optimize(starting_solution: Solution, info: ProblemInfo, tabu_length=10, iterations=200, raport=True):
    if raport:
        print(f"Start optymalizacji zadania:\n{starting_solution}\nz parametrami: długość tabu = {tabu_length}"
              f", ilość maksymalnych iteracji = {iterations}")
    best_solution = starting_solution
    last_solution = starting_solution
    tabu = TabuList(tabu_length)  # INICJALIZACJA TABU
    tabu.insert_elem(starting_solution)
    for i in range(iterations):
        neighbours = []  # WYWOŁANIE FUNKCJI SZUKAJĄCEJ SĄSIADÓW
        for _ in range(10):
            neighbours.append(Solution(find_neighbour(last_solution.matrix_, info), info))
        neighbours.sort(key=lambda x: x.quality_, reverse=True)
        last_solution = None
        for candidate in neighbours:
            if candidate in tabu:
                continue
            last_solution = candidate
            # DODANIE LAST CANDIDATE DO LISTY TABU
            tabu.insert_elem(last_solution)
            break
        if last_solution is None:
            print(f"Nie znaleziono kandydatów i =  {i}")
            return best_solution  # oznacza to, że nie umiemy znaleźć nowego sąsiada
        if last_solution.quality_ > best_solution.quality_:
            best_solution = last_solution
            if raport:
                print(f"Poprawa w {i} iteracji na {best_solution.quality_}")
    return best_solution
