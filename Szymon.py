import numpy as np
import random
from quality import quality, matrix2adj, find_neigbour
from dtypes import matrix_to_solve
from solution import Solution
from Jan import Tabu_list


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
    matrix[0][1] = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]  # żeby nie wychodziło 0 przesyłu
    return np.array(matrix)


def optimize(starting_solution: Solution, info: matrix_to_solve, tabu_length=10, iterations=300):
    best_solution = starting_solution
    last_solution = starting_solution
    tabu = Tabu_list(20)  # INICJALIZACJA TABU
    tabu.insert_elem(starting_solution)
    for i in range(iterations):
        neighbours = []  # WYWOŁANIE FUNKCJI SZUKAJĄCEJ SĄSIADÓW
        for _ in range(100):
            neighbours.append(Solution(find_neigbour(last_solution.matrix_, info), info))
        neighbours.sort(key=lambda x: x.quality_, reverse=True)
        final_candidate = None
        for candidate in neighbours:
            if candidate in tabu:
                continue
            final_candidate = candidate
            last_solution = candidate
            # DODANIE FINAL CANDIDATE DO LISTY TABU
            tabu.insert_elem(last_solution)
            break
        if final_candidate is None:
            print(f"Nie znaleziono kandydatów i =  {i}")
            return best_solution  # oznacza to, że umiemy znaleźć nowego sąsiada
        if final_candidate.quality_ > best_solution.quality_:
            best_solution = final_candidate
    print("Wyszedłem")
    return best_solution
