''''Write a function that combines two lists by alternatingly taking elements.
 For example: given the two lists [a, b, c] and [1, 2, 3], the function should 
 return [a, 1, b, 2, c, 3].'''

x = ["a", "b", "c"]
y = [1, 2, 3]

def combined_lists(x, y):
    z = []
    while len(x) > 0:
        z.append(x.pop(0))
        z.append(y.pop(0))
    print z
    return z

combined_lists(x, y)