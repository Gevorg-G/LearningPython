# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):

    # Переводим число в строку
    string = str(num)
    
    # Пустая строка для записи результата
    final = ''

    # Ходим по строке
    for i in range(len(string)):
        # Если больше нуля работаем
        if int(string[i]) > 0:
            # Возводим в нужную степень по позиции, добавляем плюсы и пробелы
            final += str(int(string[i]) * (10 ** (len(string) - i - 1))) + ' + '
    
    # Удаляем последние плюсы и пробелы
    final = final[:len(final)-3]

    return final

print(expanded_form(702912))