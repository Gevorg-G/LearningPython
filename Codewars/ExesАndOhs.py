# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.

def xo (s):
    x = 0
    o = 0
    
    # Переводим всё в нижний регистр
    s = s.lower()
    print(s)

    # Проверяем на наличие x и o
    for i in range(len(s)):
        if s[i] == "x":
            x += 1
        elif s[i] == "o":
            o += 1

    # Проверяем на равенство
    if x == o:
        return True
    else:
        return False


string = input("Введите ваше слово: ")

result = xo(string)
print(result)