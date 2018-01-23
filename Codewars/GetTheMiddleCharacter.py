# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

import math


# Получаем слово
word = input("Введите слово: ")

# Вычисляем и печатаем длину
wordLength = len(word)
print(wordLength)

# Проверяем, что длина правильная
if wordLength == 0 or wordLength > 200:
    print("Ваше слово не подходит")
    quit()

# Проверяем чётное ли число символов
if wordLength % 2 == 0:
    # Число символов чётное, поэтому выводим 2 символа
    symbol1 = word[int(wordLength/2) - 1]
    symbol2 = word[int(wordLength/2)]
    print(symbol1, symbol2)

else:
    # Число символов нечётное, поэтому выводим слово по середине
    symbol1 = word[int(math.floor(wordLength/2))]
    print(symbol1)