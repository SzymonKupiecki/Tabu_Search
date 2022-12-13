# Tabu Search
Projekt składa się następujących plików, funkcje nieużywane poza danymi plikami nie są opisane:
##### dtypes.py
Zawiera klasę ProblemInfo, która przechowuje informację o macierzy trudności, wymaganiach budynków
oraz kosztach i przesyłach kabli
##### solution_matrix.py
Zawiera generator przykładowych macierzy rozwiązań (sample_matrix_generator)
oraz funkcję konwertującą tą macierz na macierz oraz listę sąsiedztwa (matrix2adj)
##### quality.py
Zawiera funkcję kryterialną (quality), która oblicza wskaźnik jakości zadanej macierzy
##### solution.py
Zawiera klasę Solution, która przechowuje macierz rozwiązań oraz oblicza jej wskaźnik jakości,
oraz umożliwia jej łatwe wypisywanie a także funkcję zwracającego losowego sąsiada danego rozwiązania (find_neighbour)
##### tabu_list.py
Zawiera klasę TabuList, która udostępnia funkcjonalność kolejki FIFO dla klasy Solution z zadaną długością
oraz możliwości sprawdzenia czy dany obiekt jest w konkretnej liście
##### main_loop.py
Zawiera funkcję wykonującą algorytm tabu search (optimize)
