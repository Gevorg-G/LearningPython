# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldWay !

import re

def pig_it(text):
    # Документация по регуляркам: 
    # https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F
    # 
    # \b —  граница слова
    # 
    # Про группировку:
    # https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F#%D0%93%D1%80%D1%83%D0%BF%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0
    # \w — найдёт первую букву в слове
    # (\w) — используется для группировки, запишет в \1 найденный символ
    # \w* — найдёт все остальные символы в строке, если они есть
    # (\w*) — используется для группировки, запишет в \2 найденный символ
    # \2\1ay — соединит остальную часть слова, потом первый символ, потом ay
    return re.sub(r'\b(\w)(\w*)\b', r'\2\1ay', text)

print (pig_it("asda, asda,"))