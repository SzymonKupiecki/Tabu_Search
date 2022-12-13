from dtypes import ProblemInfo
from solution import Solution, find_neighbour
from tabu_list import TabuList


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
            neighbours.append(Solution(find_neighbour(last_solution, info), info))
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
