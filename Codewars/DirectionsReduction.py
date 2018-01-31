# Task
# Write a function dirReduc which will take an array of strings and returns an 
# array of strings with the needless directions removed (W<->E or S<->N side by side).

# Examples
# dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH", @"WEST"]); // => @[@"WEST"]
# dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH"]); // => @[]
# See more examples in "Example Tests"
# Note
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. 
# "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. 
# Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

# Другие решения: https://www.codewars.com/kata/550f22f4d758534c1100025a/solutions/python

def dirReduc(arr):
    # Массив с примерами
    sample = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["WEST", "EAST"], ["EAST", "WEST"]]

    # Ходим по миссиву до предпоследнего элемента
    # Потому что проверяем предпоследний и последний
    for i in range(len(arr)-1):
        # Ходим по примерам
        for j in range(len(sample)):
            # Просто для наглядности печатаем проверяемые элементы и с какими примерами сравниваем
            # Из-за непонятных причин надо писать +2, чтобы проверялся элемент перед первым
            print(arr[i:i+2], sample[j])
            # Проверяем на равенство кусок массива и пример
            if arr[i:i+2] == sample[j]:
                # Удаляем кусок массива
                del arr[i:i+2]
                # После удаления вызываем функцию, чтобы пойти по обновлённому массиву
                dirReduc(arr)
    return arr

print(dirReduc (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))