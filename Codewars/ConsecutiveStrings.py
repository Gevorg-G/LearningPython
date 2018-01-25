# You are given an array strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    # Проверяем ненулевой ли список
    # Проверяем не длиннее ли он k
    # И положительное ли k
    if len(strarr) == 0 or len(strarr) < k or k <= 0:
        return ""
    
    else:
        # В пустой массив будем писать суммы последовательностей строк
        summary = []
        
        # Ходим по списку от 0 до длины массива минус нужная последовательность элементов
        for i in range(len(strarr) - k + 1):
            
            # Создаём новый пустой элемент в массиве
            summary.append (0)
            
            # В этом цикле ходим от текущей точки (i) до нужной длины последовательностей символов
            for j in range(i, k + i):
                # Если совпадает — записываем в массив
                summary[i] += len(strarr[j])

        # Пустая строка, в которую мы запишем финальный результат
        strFinal = ''

        # Ищем индекс максимального элемента
        # Ходим от этого элемента и до нужной длины, суммируя строки
        for i in range(summary.index(max(summary)), summary.index(max(summary)) + k):
            strFinal += strarr[i]
    
    return strFinal


print (longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))