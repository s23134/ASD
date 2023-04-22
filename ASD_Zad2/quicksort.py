from partition import partition

def quicksort(A, i, j):
    if i < j:
        p = partition(A, i, j)
        print("Po podziale w indeksie", p, "tablica wygląda następująco:", A)
        quicksort(A, i, p-1)
        quicksort(A, p+1, j)
