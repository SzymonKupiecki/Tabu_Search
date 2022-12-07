
def dfs(adj_list):
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
                        # return cycle_exists
    return visited


def transfer_list(max_conncetion_matrix, adj_lst, cost_tuple):
    usage_lst = [0 for i in range(len(adj_lst.keys()))]
    visiting_order = dfs(adj_lst)
    last_elem_indeks = len(visiting_order) - 1
    usage_lst[0] = 10**10  # server has infinite
    current_index = 1
    parent_index = 0
    while current_index <= last_elem_indeks:
        current_vertex = visiting_order[current_index]
        parent_vertex = visiting_order[parent_index]
        zadany_przesyl_rodzica, _, _ = cost_tuple[parent_vertex]
        usage_lst[current_vertex] = min(max_conncetion_matrix[current_vertex][parent_vertex],
                                        usage_lst[parent_vertex] - zadany_przesyl_rodzica)

        if usage_lst[current_vertex] < 0:
            usage_lst[current_vertex] = 0

        parent_index = current_index
        current_index = current_index + 1
        if current_index > last_elem_indeks:
            break

        if current_index not in adj_lst[parent_index]:
            parent_index = parent_index - 1
            # temp_parent_vertex
            p, _, _ = cost_tuple[parent_vertex + 1]
            usage_lst[parent_index] += max(usage_lst[parent_index + 1] - p, 0)

    return usage_lst


