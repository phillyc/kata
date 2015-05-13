'''
Write three functions that compute the sum of the numbers
in a given list using a for-loop, a while-loop, and recursion.
'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def for_loop_sum(x):
    total = 0
    for num in x:
        total += num
    print "Total from for loop: %s" % total

for_loop_sum(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def while_loop_sum(x):
    total = 0
    while len(x) > 0:
        total += x.pop()
    print "Total from while loop %s" % total

while_loop_sum(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def recursion_loop_sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + recursion_loop_sum(x[1:])

print "Total from recursion loop %s" % recursion_loop_sum(x)