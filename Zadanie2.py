def get_fibonacci(n):
    fib_1 = fib_2 = 1
    if n < 2:
        quit()
    print(fib_1, end=' ')
    print(fib_2, end=' ')
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')


get_fibonacci(10)
