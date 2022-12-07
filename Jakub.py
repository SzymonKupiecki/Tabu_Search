#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from Jan import matrix_to_solve
from Szymon import Solution

def cost_function(difficulty_matrix,connection_matrix,available_wires): #Funkcja obliczająca koszty budowy sieci
    total_cost = 0 #Całkowity koszt za budowę sieci
    cost = 0 #indeks mówiący o koszcie danego kabla
    for id_verse,connection in enumerate(connection_matrix): #Iteracja po wszystkich połączeniach danego budynku
        for id_row,wires in enumerate(connection): #Iteracja po wszystkich rodzajach kabla w danym połączeniu
            if wires != np.inf: #Jeżeli połączenie istnieje to oblicz koszty jego utworzenia
                for id_wire,amount_of_wire in enumerate(wires):
                    #Dodaj do całkowitego kosztu koszt jednego połączenia
                    total_cost += available_wires[id_wire][cost] * amount_of_wire * difficulty_matrix[id_verse][id_row]
    return total_cost

def estimate_of_benefits_losses(vector_of_beneficts_losses, conection_matrix, vector_of_request,available_wires): #Funkcja szacująca zyzki i straty generowane z sieci
    benefits = 0 #Indeks zysków
    losses = 1 #Indeks strat
    transmition = 1 #Indeks przesyłu danego rodzaju kabla
    total_balance = 0 #Całkowity bilans
    for dorm_id,conections in enumerate(conection_matrix): #Iterowanie po każdym akademiku
        total_transmit = 0 #Całkowity przesył dla danego akademika
        for neighbour in conections: #Iteracja po połączeniach  akademikiem
            if neighbour != np.inf: #Jeżeli połączenie istnieje to dodaj jego przesył do całkowitego przesyłu
                for id_wire,amount_of_wire in enumerate(neighbour):
                    total_transmit += available_wires[id_wire][transmition] * amount_of_wire
        if total_transmit >= vector_of_request[dorm_id]: total_balance += vector_of_beneficts_losses[dorm_id][benefits] #Dodaj zyski jeżeli spełniony wymagany przesył
        else: total_balance -= vector_of_beneficts_losses[dorm_id][losses] #W przeciwnym przypadku odejmij od całkowitego bilansu straty
    return total_balance

def trasnsmission_allocation(solution: Solution,Matrix_to_solve: matrix_to_solve,vector_of_request):
    stack = [0]
    visited = list()
    list_of_transmission = vector_of_request
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for u_idx,u in enumerate(Matrix_to_solve.connection_matrix[v]):
                if u is not None and u != np.inf:
                    if u not in visited:
                        list_of_transmission[v] += list_of_transmission[u_idx]
                        stack.append(u_idx)
                        visited.append(u)

def transmission_allocation_2(solution: Solution,Matrix_to_solve: matrix_to_solve,vector_of_request):
    def dfs(node,visited,Matrix_to_solve: matrix_to_solve,vector_of_request):
        if node not in visited:
            visited.append(node)
            for ngh_idx,neighbour in enumerate(Matrix_to_solve.connection_matrix[node]):
                if neighbour is not None and neighbour != np.inf:
                    result = dfs(ngh_idx,visited,Matrix_to_solve,vector_of_request)
                    if result: vector_of_request[node] += result
            return vector_of_request[node]

def matrix_of_max_transfer(Matrix_to_solve:matrix_to_solve):
    matrix_of_max_transfer = np.zeros(Matrix_to_solve.connection_matrix)
    for id_dorm,dormitory in enumerate(Matrix_to_solve.connection_matrix):
        for id_connect,connection in enumerate(dormitory):
            max_transfer = 0
            if connection is not None and connection != np.inf:
                for id_wire,wire in enumerate(connection):
                    max_transfer += Matrix_to_solve.cable_vector[id_wire][1]
                matrix_of_max_transfer[id_dorm][id_connect] = max_transfer
    for i in range(1, len(matrix_of_max_transfer)):
        for j in range(i):
            matrix_of_max_transfer[j][i] = matrix_of_max_transfer[i][j]
    return matrix_of_max_transfer