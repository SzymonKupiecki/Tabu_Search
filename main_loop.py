from dtypes import ProblemInfo, ChangeType
from solution import Solution, find_neighbour_transfer, find_neighbour_add_connection, forbidden_moves\
    , find_neighbour_del_connection
from tabu_list import TabuList


def optimize(starting_solution: Solution, info: ProblemInfo, tabu_length=10, iterations=200, raport=True,
             number_of_neighbours_in_iteration=20, multiple_deletions=5):
    history = [starting_solution.quality_]
    changes_history = []
    if raport:
        print(f"Start optymalizacji zadania:\n{starting_solution}\nz parametrami: długość tabu = {tabu_length}"
              f", ilość iteracji = {iterations}")
    best_solution = starting_solution  # variable to store best solution
    last_solution = starting_solution  # variable to store solution that was taken in last correct iteration
    tabu = TabuList(tabu_length)  # initialization of tabu list
    for i in range(iterations):
        neighbours = []  # list to store neighbours found in iteration
        for _ in range(number_of_neighbours_in_iteration//3):  # finding neighbours, 33% of each type
            neighbours.append(find_neighbour_transfer(last_solution, info))
            neighbours.append(find_neighbour_del_connection(last_solution, info, 1))
            added_connection = find_neighbour_add_connection(last_solution, info)
            if added_connection is not None:
                neighbours.append(added_connection)
        if multiple_deletions >= 2:
            for del_amount in range(2, multiple_deletions+1):
                neighbours.append(find_neighbour_del_connection(last_solution, info, del_amount))
        neighbours.sort(key=lambda x: x.quality_, reverse=True)  # sort by quality
        next_solution = None
        for candidate in neighbours:
            #  criterion of aspiration - if found solution is better than best take it despite it's forbidden by tabu
            if ((candidate not in tabu) and candidate != last_solution) or candidate.quality_ > best_solution.quality_:
                next_solution = candidate  # take solution that fulfills requirements
                tabu.insert_elem(forbidden_moves(last_solution))  # forbid all changes that will return to prev solution
                history.append(next_solution.quality_)
                changes_history.append(next_solution.changes_)
                break
        if next_solution is None:
            txt = f"Nie znaleziono kandydatów i =  {i}"
            # for x in neighbours:
            #     txt += f" chng = {x.changes_} tabu? {x in tabu}"
            # print(tabu.tab)
            print(txt)
            tabu.insert_elem([(-1, -1, ChangeType.INCREASE)])
            history.append(history[-1])
            continue  # we don't find correct neighbour, so we try again
        last_solution = next_solution  # if we found new solution assign it to proper variable
        if last_solution.quality_ > best_solution.quality_:
            best_solution = last_solution
            if raport:
                print(f"Poprawa w {i} iteracji na {best_solution.quality_}")
    if raport:
        print(f"Znalezione rozwiązanie:\n{best_solution}")
    return best_solution, history, changes_history
