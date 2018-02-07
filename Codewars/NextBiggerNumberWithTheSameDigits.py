# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# If no bigger number can be composed using those digits, return -1:

# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

import itertools

def next_bigger(n):
    m = sorted(list(str(n)))
    b = -1
    for i in itertools.permutations([x for x in m], len(str(n))):
        print (i)
        a = int(''.join(i))
        if a > n and (a < b or b == -1):
            return a
    return b

print(next_bigger(1234567890))