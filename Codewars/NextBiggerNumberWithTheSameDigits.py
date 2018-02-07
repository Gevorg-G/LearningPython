# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# If no bigger number can be composed using those digits, return -1:

# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

import time
s = time.time()
from itertools import permutations
print(time.time()-s)

def next_bigger(n):
    m = list(str(n))

    for i in range(len(m)-1, 0 , -1):
        arr = sorted(list(m[len(m)-1-i:]))
        for j in permutations(arr):
            if int(''.join(j)) > n:
                return(int(''.join(j)))
    return -1


# def next_bigger(n):
#     m = list(str(n))
#     mp = list(int(''.join(l)) for l in itertools.permutations(m))
    
#     min_n = float("inf")
#     for l in itertools.permutations(m):
#         d = int(''.join(l))
#         if d > n and d < min_n:
#             min_n = d
    
#     if min_n == n or float("inf") == min_n:
#         return -1
#     return min_n

start = time.time()
print(next_bigger(1234567890))
print (time.time()-start)
