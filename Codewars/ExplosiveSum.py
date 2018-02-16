# How many ways can you make the sum of a number?
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

import time
# import sympy

# def exp_sum(n):
#     if n < 0:
#         return 0;
#     else:
#         return sympy.ntheory.npartitions(n)


def splitter(number):
    tempArray = []
    for i in range(number):
        tempArray.append([number-i, i])
    tempArray.pop(0)
    
    return tempArray

def exp_sum(number):
    if number < 0:
        return 0
    elif number == 0:
        return 1
    
    partitions = []
    for i in range(number):
        partitions.append([number-i, i])

    j = 0 
    while j != len(partitions):
        for k in range(1, len(partitions[j])):
            if partitions[j][k] > 1:
                for l in splitter(partitions[j][k]):
                    partitions.insert(j+1, [])
                    partitions[j+1] += partitions[j][:k]
                    partitions[j+1] += l
                    partitions[j+1] += partitions[j][k+1:]
                partitions[j].sort(reverse=True)
        j += 1
    
    result = []
    
    for m in partitions:
        if m not in result:
            result.append(m)
    
    return len(result)

print (exp_sum(-1))
print (exp_sum(0))
print (exp_sum(1))
print (exp_sum(2))
print (exp_sum(3))
print (exp_sum(4))
print (exp_sum(5))
print (exp_sum(10))
print (exp_sum(20))

# start = time.time()

# print (time.time()-start)