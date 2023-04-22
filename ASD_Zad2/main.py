from quicksort import quicksort
from partition import partition
import random

A = [random.randint(1, 100) for _ in range(50)]

print("Przed sortowaniem: ", A)

quicksort(A, 0, len(A)-1)
print("Po sortowaniu: ", A)