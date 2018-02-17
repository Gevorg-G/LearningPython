# https://www.codewars.com/kata/catching-car-mileage-numbers/train/python

def isGood(number, awesome_phrases):
    digits = [int(digit) for digit in str(number)]

    if (number % 100 == 0 
        or len(list(set(digits))) == 1 
        or str(number) in '1234567890 9876543210'
        or str(number) == str(number)[::-1]
        or number in awesome_phrases):
        return 2
    else:
        return 0

def is_interesting(number, awesome_phrases):
    result = []
    
    if number < 98:
        return 0
    elif number == 98 or number == 99:
        return 1

    for i in range(0, 3):
        result = isGood(number+i, awesome_phrases)

        if result == 2 and i == 0:
            return 2
        elif result == 2 and i > 0:
            return 1

    return 0

print(is_interesting(120, [1337, 256]))