import random
import time
from quicksort import *
from countingsort import *
from heapsort import *

# Generowanie losowej tablicy liczb całkowitych większych od zera
array_size = 300000  # Rozmiar tablicy
random_array = [random.randint(1, array_size) for _ in range(array_size)]

# Sortowanie i pomiar czasu dla quicksort
start_time = time.time()
quicksort_result = quicksort(random_array)
quicksort_time = time.time() - start_time

# Sortowanie i pomiar czasu dla countingsort
start_time = time.time()
countingsort_result = countingsort(random_array)
countingsort_time = time.time() - start_time

# Sortowanie i pomiar czasu dla heapsort
start_time = time.time()
heapsort_result = heapsort(random_array)
heapsort_time = time.time() - start_time

# Wyświetlanie wyników
print("Czas sortowania dla quicksort:", quicksort_time)
print("Czas sortowania dla countingsort:", countingsort_time)
print("Czas sortowania dla heapsort:", heapsort_time)