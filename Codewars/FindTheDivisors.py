# Create a function named divisors/Divisors that takes an integer 
# and returns an array with all of the integer's divisors(except for 1 and the number itself). 
# If the number is prime return the string '(integer) is prime' (null in C#) 
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

import math

def divisors (integer):
    # Проверяем на 1
    if integer == 1:
        print("1 is prime number")
        quit()

    # Инициализируем массив, в который будем писать делители
    divArray = []
    
    # Итерирем по списку от 2 (1 не считаем) до половины числа + 1
    for i in range(2, int(math.floor(integer/2)+1)):
        # Проверяем делится ли нацело
        if integer % i == 0:
            # Если да, то записываем в массив в конец
            divArray.append(i)
    
    # Если массив нулевой, то число простое и мы выходим из программы
    if len(divArray) == 0:
        print("Your number is prime")
        quit()
    # Если массив ненулевой, то возвращаем его обратно
    else:
        # Проверяем не получили ли мы нулевой массив. Если нет — печатаем массив
        if len(divArray) > 0:
            for j in range(len(divArray)):
                print(divArray[j])
        return divArray

# Просим ввести число
integer = int(input("Введите число: "))

# Передаём число в функцию
result = divisors(integer)


