def fac(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n - 1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def square(n):
    return n * n
