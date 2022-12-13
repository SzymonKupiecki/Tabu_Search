class ProblemInfo:
    def __init__(self, hard_matrix, cable_vector, cost_tuple):
        self.num_of_buildings = len(hard_matrix)  # liczba budynków
        self.cable_vector = cable_vector  # [(koszt kabla, przesył)]
        self.cost_tuple = cost_tuple  # (żądany przesył, zysk, kara), indeks = nr budynku
        self.hard_matrix = hard_matrix  # macierz trudności
