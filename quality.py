import numpy as np
from Jan import matrix_to_solve


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


def matrix_of_max_transfer(info: matrix_to_solve, matrix: np.ndarray):
    matrix_of_max_transfer = np.zeros((len(matrix), len(matrix[0])))
    for id_dorm, dormitory in enumerate(matrix):
        for id_connect, connection in enumerate(dormitory):
            max_transfer = 0
            # if connection is not None and connection != np.inf: to było poprzednio
            if np.all(connection != 0):
                for id_wire, wire in enumerate(connection):
                    max_transfer += info.cable_vector[id_wire][1] * matrix[id_dorm][id_connect][id_wire]
                matrix_of_max_transfer[id_dorm][id_connect] = max_transfer
    for i in range(len(matrix_of_max_transfer)):
        for j in range(i+1, len(matrix_of_max_transfer)):
            matrix_of_max_transfer[j][i] = matrix_of_max_transfer[i][j]
    return matrix_of_max_transfer


def dfs(adj_list):
    visited = list()
    cycle_exists = False
    stack = [0]  # creating a stack, always start from 0
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
                        # return cycle_exists
    return visited


def transfer_list(max_connection_matrix, adj_lst, cost_tuple):
    usage_lst = [0 for i in range(len(adj_lst.keys()))]  # list to be returned
    visiting_order = dfs(adj_lst)
    last_elem_indeks = len(visiting_order) - 1
    usage_lst[0] = np.inf  # server has infinite transfer
    current_index = 1  # server have predefined transfer
    parent_index = 0  # first dorm is connected to server
    while current_index <= last_elem_indeks:
        current_vertex = visiting_order[current_index]
        parent_vertex = visiting_order[parent_index]
        expected_transfer, _, _ = cost_tuple[parent_vertex]
        # take the lower - max transfer provided by cables or transfer that left after satisfying parent expectations
        transfer = min(max_connection_matrix[current_vertex][parent_vertex],
                       usage_lst[parent_vertex] - expected_transfer)
        # give calculated transfer to current vertex and take it from parent, probably can be negative
        if transfer > 0:
            usage_lst[current_vertex] += transfer
            usage_lst[parent_vertex] -= transfer
        # choosing new vertex
        parent_index = current_index
        current_index = current_index + 1
        if current_index > last_elem_indeks:
            break
        # trying to find parent for new vertex (have to go backwards until find vertex that is neighbour to current)
        current_vertex = visiting_order[current_index]
        parent_vertex = visiting_order[parent_index]
        while current_vertex not in adj_lst[visiting_order[parent_index]]:
            parent_index = parent_index - 1
            temp_prev_parent_vertex = visiting_order[parent_index + 1]
            temp_act_parent_vertex = visiting_order[parent_index]
            p, _, _ = cost_tuple[temp_prev_parent_vertex]
            # when going backwards have to give additional transfer back
            usage_lst[temp_act_parent_vertex] += max(usage_lst[temp_prev_parent_vertex] - p, 0)
            usage_lst[temp_prev_parent_vertex] -= max(usage_lst[temp_prev_parent_vertex] - p, 0)

    return usage_lst


def estimate_of_benefits_losses(transfer_lst: list, matrix: matrix_to_solve):
    vector_of_request = matrix.cost_tuple
    request = 0
    benefits = 1  # Indeks zysków
    losses = 2  # Indeks strat
    total_balance = 0  # Całkowity bilans
    for dorm_id, transfer in enumerate(transfer_lst):
        if transfer >= vector_of_request[dorm_id][request]: total_balance += vector_of_request[dorm_id][benefits]
        else: total_balance -= vector_of_request[dorm_id][losses]
    return total_balance


def cost_function(info: matrix_to_solve, matrix: np.ndarray):  # Funkcja obliczająca koszty budowy sieci
    difficulty_matrix = info.hard_matrix
    connection_matrix = matrix
    available_wires = info.cable_vector
    total_cost = 0  # Całkowity koszt za budowę sieci
    cost = 0  # indeks mówiący o koszcie danego kabla
    for id_verse, connection in enumerate(connection_matrix):  # Iteracja po wszystkich połączeniach danego budynku
        for id_row, wires in enumerate(connection):  # Iteracja po wszystkich rodzajach kabla w danym połączeniu
            # if wires != np.inf:  # Jeżeli połączenie istnieje to oblicz koszty jego utworzenia to było poprzednio
            if np.all(wires != 0):  # Jeżeli połączenie istnieje to oblicz koszty jego utworzenia
                for id_wire, amount_of_wire in enumerate(wires):
                    # Dodaj do całkowitego kosztu koszt jednego połączenia
                    total_cost += available_wires[id_wire][cost] * amount_of_wire * difficulty_matrix[id_verse][id_row]
    return total_cost


def quality(info: matrix_to_solve, matrix: np.ndarray):
    # polaczyc wszytskie powyzsze
    max_connection = matrix_of_max_transfer(info, matrix)
    adj_matrix, adj_list = matrix2adj(matrix)
    transfer_lst = transfer_list(max_connection, adj_list, info.cost_tuple)
    total_bilans = estimate_of_benefits_losses(transfer_lst, info)
    total_bilans -= cost_function(info, matrix)
    return total_bilans
