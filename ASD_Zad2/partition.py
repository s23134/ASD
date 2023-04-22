def partition(A, i, j):
    pivot = A[j]
    p = i - 1
    for k in range(i, j):
        if A[k] < pivot:
            p += 1
            A[k], A[p] = A[p], A[k]
    A[p+1], A[j] = A[j], A[p+1]
    return p+1