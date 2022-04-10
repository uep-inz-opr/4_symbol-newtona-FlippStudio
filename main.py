nk = input()

list_of_numbers = nk.split(' ')


def newton_symbol(lon):
    from math import factorial
    n = int(lon[0])
    k = int(lon[1])
    return int(factorial(n)/(factorial(k) * factorial(n-k)))


print(newton_symbol(list_of_numbers))
