# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
# Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.
# Empty expression should evaluate to 0.
# Valid operations are +, -, *, /.
# You may assume that there won't be exceptional situations (like stack underflow or division by zero).

import math
import operator

operators = ['+', '-', '/', '*']

# Функция проверяет целое или дробное ли число на входе и возвращает в соответствующем типе
def intOrFloat(s):
    try:
        int(s)
        return int(s)
    except:
        # Эта проверка нужна для деление, которое всегда даёт дробное число
        # Например 4 / 2 = 2.0, а нам нужно 2
        if float(s) % 1 != 0:
            return float(s)
        return math.floor(float(s))

def calc(expr):
    # Если список пустой возвращаем 0 и показываем соответствующее сообщение
    if not expr:
        print ("Empty expression")
        return 0
    
    # Если всё же надо поработать — делим строку на список
    notation = expr.split(sep=' ')

    # Если строка длиной в 1 элемент, то возвращаем этот элемент
    if len(notation) == 1:
        # Проверяем этот единственный элемент — целое или дробное число и возвращаем результат
        return intOrFloat(notation[-1])

    # Проверяем есть ли вообще операторы в списке
    isThereAnyOperators = 0
    for i in operators:
        if i in notation:
            isThereAnyOperators = 1
    
    if isThereAnyOperators == 1:
        while len(notation) != 1:
            # Ищем индекс минимального оператора
            minIndex = -1
            for i in operators:
                if i in notation and (notation.index(i) < minIndex or minIndex == -1):
                    minIndex = notation.index(i)
            
            # Записываем наши операнды
            secondOperand = intOrFloat(notation[minIndex - 1])
            firstOperand = intOrFloat(notation[minIndex - 2])
            
            # Смотрим какое арифметическое действие нам надо выполнить
            if notation[minIndex] == '+':
                notation[minIndex] = str(intOrFloat(str(firstOperand + secondOperand)))
            elif notation[minIndex] == '-':
                notation[minIndex] = str(intOrFloat(str(firstOperand - secondOperand)))
            elif notation[minIndex] == '/':
                notation[minIndex] = str(intOrFloat(str(firstOperand / secondOperand)))
            elif notation[minIndex] == '*':
                notation[minIndex] = str(intOrFloat(str(firstOperand * secondOperand)))
            notation.pop(minIndex-1)
            notation.pop(minIndex-2)
        return intOrFloat(notation[-1])
    else:
        return intOrFloat(notation[-1])

print(calc(""))
print(calc("1 2 3"))
print(calc("1 2 3.5"))
print(calc("1 3 +"))
print(calc("1 3 *"))
print(calc("1 3 -"))
print(calc("4 2 /"))