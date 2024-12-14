def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = a+b, a

gen = fib(5)
for i in gen:
    print(i)