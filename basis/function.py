def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def product(x, *y):
    sum = 1
    for i in y:
        sum = sum * i
    return x * sum

print(my_abs(-9))
