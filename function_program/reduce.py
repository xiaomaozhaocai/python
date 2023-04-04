from functools import reduce

def add(x, y):
    return x+y

print(reduce(add,[1,2,3,4]))

