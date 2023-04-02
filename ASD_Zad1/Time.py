import timeit
from Tables import *
from Insertion import insertion_sort

def measure_time():
    for i, tab in enumerate([tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, tab_7, tab_8, tab_9, tab_10]):
        n = len(tab)
        t = timeit.timeit(lambda: insertion_sort(tab), number=1)
        fn = n if i < 5 else n^2
        print(f"Fn={n}, Tn={t*1000}[ms], Fn/Tn={fn/t}")
        
measure_time()