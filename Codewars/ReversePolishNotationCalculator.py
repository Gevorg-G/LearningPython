# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
# Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.
# Empty expression should evaluate to 0.
# Valid operations are +, -, *, /.
# You may assume that there won't be exceptional situations (like stack underflow or division by zero).

import math
import operator

operators = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}

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
  # Делим строку на символы
  # Забавная вещь — этот же самый код не работает, если написать expr.split(' ')
  notation = expr.split()
  # Создаём промежуточный массив
  # 0 нужен на случай передачи пустой строки
  resultingArray = [0]

  # Ходим по символам
  for i in notation:
    # Если символ является оператором
    if i in operators:
      # То из промежуточного массива вытаскиваем операнды. 
      # Сначала второй, потом первый, потому что pop() удаляем из конца
      secondOperand = resultingArray.pop()
      firstOperand = resultingArray.pop()
      # Считаем, вытаскивая операцию из словаря
      resultingArray.append(operators[i](firstOperand, secondOperand))
    else:
      # Если же это не оператор, а операнд, то записываем его в массив
      resultingArray.append(intOrFloat(i))
  # В итоге вытаскиваем последний элемент массива, который и будет искомым результатом
  return resultingArray.pop()

print(calc(""))
print(calc("1 2 3"))
print(calc("1 2 3.5"))
print(calc("1 3 +"))
print(calc("1 3 *"))
print(calc("1 3 -"))
print(calc("4 2 /"))
print(calc("5 1 2 + 4 * + 3 -"))