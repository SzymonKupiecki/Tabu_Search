#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

def Cost_function(difficulty_matrix,connection_matrix,available_wires):
    total_cost = 0
    cost = 0
    for id_verse,connection in enumerate(connection_matrix):
        for id_row,wires in enumerate(connection):
            if wires != np.inf:
                for id_wire,amount_of_wire in enumerate(wires):
                    total_cost += available_wires[id_wire][cost] * amount_of_wire * difficulty_matrix[id_verse][id_row]
    return total_cost

def Estimate_of_benefits_losses(vector_of_beneficts_losses, conection_matrix, vector_of_request,available_wires):
    benefits = 0
    losses = 1
    transmition = 1
    total_balance = 0
    for dorm_id,conections in enumerate(conection_matrix):
        total_transmit = 0
        for neighbour in conections:
            if neighbour != np.inf:
                for id_wire,amount_of_wire in enumerate(neighbour):
                    total_transmit += available_wires[id_wire][transmition] * amount_of_wire
        if total_transmit >= vector_of_request[dorm_id]: total_balance += vector_of_beneficts_losses[dorm_id][benefits]
        else: total_balance -= vector_of_beneficts_losses[dorm_id][losses]
    return total_balance


