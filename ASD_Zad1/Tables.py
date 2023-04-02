import random

# generowanie 5 tablic posortowanych rosnąco

tab_1 = sorted([i for i in range(1, 4001)])
tab_2 = sorted([i for i in range(1, 8001)])
tab_3 = sorted([i for i in range(1, 16001)])
tab_4 = sorted([i for i in range(1, 32001)])
tab_5 = sorted([i for i in range(1, 64001)])

# generowanie 5 tablic posortowanych malejąco

tab_6 = sorted([i for i in reversed(range(1, 4001))])
tab_7 = sorted([i for i in reversed(range(1, 8001))])
tab_8 = sorted([i for i in reversed(range(1, 16001))])
tab_9 = sorted([i for i in reversed(range(1, 32001))])
tab_10 = sorted([i for i in reversed(range(1, 64001))])