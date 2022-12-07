from quality import transfer_list

max_connection = [[0, 90, 0, 0, 40, 0],
                  [90, 0, 30, 30, 0, 0],
                  [0, 30, 0, 0, 0, 10],
                  [0, 30, 0, 0, 0, 0],
                  [40, 0, 0, 0, 0, 0],
                  [0, 0, 10, 0, 0]]

lst_tup = [(0, 0, 0), (40, 15, 15), (20, 15, 15), (80, 15, 15), (20, 15, 15), (20, 15, 15)]

matrix = {
    0: [1, 4],
    1: [0, 2, 3],
    2: [1, 5],
    3: [1],
    4: [0],
    5: [2]
}

hope = transfer_list(max_connection, matrix, lst_tup)
print(hope)
