# Which is faster, pop(0) or reverse, pop, reverse?

z = []
for x in range(100000):
    z.append(x)

# while len(z) > 0:
#     z.pop(0)

while len(z) > 0:
    z.reverse()
    z.pop()
    z.reverse()


