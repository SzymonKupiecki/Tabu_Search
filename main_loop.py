from dtypes import ProblemInfo
from solution import Solution, find_neighbour_transfer, find_neighbour_connection, forbidden_moves
from tabu_list import TabuList


def optimize(starting_solution: Solution, info: ProblemInfo, tabu_length=10, iterations=200, raport=True,
             number_of_neighbours_in_iteration=20):
    if raport:
        print(f"Start optymalizacji zadania:\n{starting_solution}\nz parametrami: długość tabu = {tabu_length}"
              f", ilość iteracji = {iterations}")
    best_solution = starting_solution  # variable to store best solution
    last_solution = starting_solution  # variable to store solution that was taken in last correct iteration
    tabu = TabuList(tabu_length)  # initialization of tabu list
    for i in range(iterations):
        neighbours = []  # list to store neighbours found in iteration
        for _ in range(number_of_neighbours_in_iteration//2):  # finding neighbours, 50% of each type
            neighbours.append(find_neighbour_transfer(last_solution, info))
            unoptimized_shit = find_neighbour_connection(last_solution, info)
            if unoptimized_shit is not None:
                neighbours.append(unoptimized_shit)
        neighbours.sort(key=lambda x: x.quality_, reverse=True)  # sort by quality
        next_solution = None
        for candidate in neighbours:
            #  criterion of aspiration - if found solution is better than best take it despite it's forbidden by tabu
            if candidate in tabu and candidate.quality_ < best_solution.quality_:
                continue
            next_solution = candidate  # take solution that fulfills requirements
            tabu.insert_elem(forbidden_moves(last_solution))  # forbid all changes that will return to previous solution
            break
        if next_solution is None:
            print(f"Nie znaleziono kandydatów i =  {i}")
            continue  # we don't find correct neighbour, so we try again
        last_solution = next_solution  # if we found new solution assign it to proper variable
        if last_solution.quality_ > best_solution.quality_:
            best_solution = last_solution
            if raport:
                print(f"Poprawa w {i} iteracji na {best_solution.quality_}")
    if raport:
        print(f"Znalezione rozwiązanie:\n{best_solution}")
    return best_solution
