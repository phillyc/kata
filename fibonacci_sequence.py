'''Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. As an example, 
here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.'''
a = 0
b = 1
def fib(a, b):
    print a
    print b
    for i in range(100):
        t = a + b
        print t
        a = b
        b = t
fib(a, b)