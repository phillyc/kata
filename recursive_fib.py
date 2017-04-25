"Calculates the nth Fibonacci number."

# Create a memoization cache so our recursion is faster.
fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib_cache[n] = fib(n-1) + fib(n-2)
        return fib(n-1) + fib(n-2)

for n in range(1, 501):
    print "%s : %s" % (n, fib(n))