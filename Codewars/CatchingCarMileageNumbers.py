# https://www.codewars.com/kata/catching-car-mileage-numbers/train/python

def followedByZero(number):
    if number % 100 == 0:
        return 2
    else:
        return 0


def sameNumbers(digits):
    if len(list(set(digits))) == 1:
        return 2
    else:
        return 0


def incrementing(digits):
    comparisons = []
    
    for i in range(1, len(digits)):
        if digits[i] == 0 and digits[i-1] == 9:
            comparisons.append(1)
        else:
            comparisons.append(digits[i] - digits[i-1])
    
    if list(set(comparisons))[0] == 1 and len(list(set(comparisons))) == 1:
        return 2
    else:
        return 0


def decrementing(digits):
    comparisons = []
   
    for i in range(1, len(digits)):
        if digits[i] == 0 and digits[i-1] == 1:
            comparisons.append(-1)
        else:
            comparisons.append(digits[i] - digits[i-1])
   
    if list(set(comparisons))[0] == -1 and len(list(set(comparisons))) == 1:
        return 2
    else:
        return 0


def palindrome(digits):
    comparisons = []
    
    for i in range(len(digits)//2):
        comparisons.append(digits[i] - digits[-1-i])
    
    if list(set(comparisons))[0] == 0 and len(list(set(comparisons))) == 1:
        return 2
    else:
        return 0

def matchPhrases(number, awesome_phrases):
    if number in awesome_phrases:
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
        digits = [int(digit) for digit in str(number+i)]
        result.append(followedByZero(number+i))
        result.append(sameNumbers(digits))
        result.append(incrementing(digits))
        result.append(decrementing(digits))
        result.append(palindrome(digits))
        result.append(matchPhrases(number+i, awesome_phrases))

        if max(result) == 2 and i == 0:
            return 2
        elif max(result) == 2 and i > 0:
            return 1

    return 0

print(is_interesting(11209, [1337, 256]))