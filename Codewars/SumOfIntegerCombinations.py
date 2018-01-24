# Consider the array [3,6,9,12]. 
# If we generate all the combinations with repetition that sum to 12, we get 5 combinations: [12], [6,6], [3,9], [3,3,6], [3,3,3,3]. 
# The length of the sub-arrays (such as [3,3,3,3] should be less than or equal to the length of the initial array ([3,6,9,12]).
# Given an array of positive integers and a number n, count all combinations with repetition of integers that sum to n.

import itertools

# Улучшенное решение — не делать массив массивов
def find(arr, n):
    
    # Счётчик числа комбинаций
    combinations = 0
    
    # Итерируем от 0 до длины списка +1
    for i in range(len(arr) + 1):
        # Итерируем по массиву комбинаций чисел
        for k in itertools.combinations_with_replacement(arr, i):
            # Если сумма строки массива совпадает, то увеличиваем счётчик
            if (sum(k) == n):
                combinations += 1
    return combinations

print (find([3,6,9,12,14,18],30))


# Старое решение
# def find(arr, n):
#     finalArr = []
    
#     # С помощью итератора делаем получаем список всех возможных комбинаций
#     for i in range(1, len(arr)+1):
#         finalArr.append([o for o in itertools.combinations_with_replacement(arr, i)])
    
#     # Счётчик числа комбинаций
#     combinations = 0

#     # Итерируем массиву массивов
#     for j in range(len(finalArr)):
#         for k in range(len(finalArr[j])):
#             if (sum(finalArr[j][k]) == n):
#                 combinations += 1
#     return combinations
