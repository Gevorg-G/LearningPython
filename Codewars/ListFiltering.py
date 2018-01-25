# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):

    # Создаём пустой массив, в него будем писать список
    finalList = []

    # Бегаем по массиву
    for i in range(len(l)):
        # Проверяем является ли числом
        if isinstance(l[i], int):
            # Если да — записываем в массив
            finalList.append(l[i])
    return finalList

print(filter_list([1,2,3,'b','c']))