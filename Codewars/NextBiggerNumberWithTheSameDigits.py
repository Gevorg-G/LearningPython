# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# If no bigger number can be composed using those digits, return -1:

# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

import itertools
import time

def next_bigger(n):
    m = list(str(n))

    for i in range(len(m)-1, 0 , -1):
        arr = sorted(list(m[len(m)-1-i:]))
        for j in itertools.permutations(arr):
            if int(''.join(j)) > n:
                return(int(''.join(j)))
    return -1

start = time.time()
print(next_bigger(1234567890))
print (time.time()-start)