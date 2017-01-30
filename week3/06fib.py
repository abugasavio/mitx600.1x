"""
Here we have two versions of fib. One using memoization and the other not doing that

"""


def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 2) + fib(n - 1)


def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        fibo = fib_efficient(n - 2, d) + fib_efficient(n - 1, d)
        d[n] = fibo
        return fibo

d = {1: 1, 2: 2}
arg = 6

numFibCalls = 0
print(fib(arg))
print('Num of calls', numFibCalls)

numFibCalls = 0
print(fib_efficient(arg, d))
print('Num of calls', numFibCalls)
