# Tabu Search
Projekt składa się następujących plików, funkcje nieużywane poza danymi plikami nie są opisane:
##### dtypes.py
Zawiera klasę ProblemInfo, która przechowuje informację o macierzy trudności, wymaganiach budynków
oraz kosztach i przesyłach kabli oraz typ wyliczeniowy oznaczający typ zmiany rozwiązania ChangeType
##### solution_matrix.py
Zawiera generator przykładowych macierzy rozwiązań (sample_matrix_generator)
oraz funkcję konwertującą tą macierz na macierz oraz listę sąsiedztwa (matrix2adj)
##### quality.py
Zawiera funkcję kryterialną (quality), która oblicza wskaźnik jakości zadanej macierzy
##### solution.py
Zawiera klasę Solution, która przechowuje macierz rozwiązań oraz oblicza jej wskaźnik jakości,
oraz umożliwia jej łatwe wypisywanie a także funkcje zwracające losowego sąsiada danego rozwiązania
różnych typów (find_neighbour_transfer, find_neighbour_connection).
Posiada także funkcję zwracającą ruchy powodujące powrót do danego rozwiązania.
##### tabu_list.py
Zawiera klasę TabuList, która udostępnia funkcjonalność kolejki FIFO dla ruchów zabronionych z zadaną długością
oraz możliwości sprawdzenia czy dany ruch jest w konkretnej liście
##### main_loop.py
Zawiera funkcję wykonującą algorytm tabu search (optimize)
