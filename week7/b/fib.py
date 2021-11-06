def fib_naive(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib(n, fn_minus_1=1, fn_minus_2=0):
    if n == 0:
        return None
    else:
        value = fn_minus_1 + fn_minus_2
        print(value)
        fn_minus_2 = fn_minus_1
        fn_minus_1 = value
        return fib(n-1, fn_minus_1, fn_minus_2)

fib(10)
