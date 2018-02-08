# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# If no bigger number can be composed using those digits, return -1:

# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

def next_bigger(n):
    # Делим число на список символов
    m = list(str(n))

    # Ходим по списку с конца — это оптимальный способ найти следующее число, которое минимально больше входящего
    # Начинаем с подстроки в 2 символа, заканчиваем подстрокой в длину числа
    for i in range(len(m)-2, -1 , -1):
        # Делаем отсортированный список из уникальных элементов по текущей строке
        substringSet = sorted(list(set(m[i:])))
        # Получаем индекс первого элемента подстроки в этом списке
        indexOfSubstringFirstElement = substringSet.index(m[i])
        
        # Это просто отсортированная подстрока. В будущем она понадобится для склейки
        substringSorted = sorted(m[i:])
        
        # Проверяем не является ли первый символ в подстроке последним символом substringSet
        if indexOfSubstringFirstElement != len(substringSet) - 1:
            # Если это не так, то тогда мы из набора уникальных цифр берём следующее цифру, которая больше текущей
            biggerDigit = substringSet[substringSet.index(m[i])+1]
            # Удаляем символ, который будем ставить в начало подстроки из substringSorted
            substringSorted.remove(biggerDigit)
            # Склеиваем строку
            # ''.join(m[:i]) — это левая часть числа, которая не входит в рассматриваемую подстроку
            # biggerDigit — цифра, которая позволит нам получить минимальное число, большее, чем входящее
            # ''.join(substringSorted) — оставшийся кусок числа, без biggerDigit
            numberToCompare = int(''.join(m[:i]) + biggerDigit + ''.join(substringSorted))
            return numberToCompare
    return -1

print(next_bigger(12))