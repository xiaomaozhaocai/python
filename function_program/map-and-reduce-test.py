from functools import reduce

L1 = ['adam', 'LISA', 'barT']
def normalize(list):
    return list[0].upper()+list[1:].lower()

L2 = list(map(normalize, L1))
print(L2)

def prod(x,y):
    return x*y
print(reduce(prod,[3, 5, 7, 9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
def str2float(s):
    s_int,s_float=s.split(".")
    return str2int(s_int+s_float)/10**len(s_float)