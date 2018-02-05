# Find the number of divisors of a positive integer n.

def divisors(n):
    if n == 0:
        return 0

    result = []
    for i in range (1, (n//2) + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return len(result)


print (divisors(8))