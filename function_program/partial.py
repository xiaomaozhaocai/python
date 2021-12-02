import functools
import sys

int2 = functools.partial(int,base=2)
print(int2('1000'))

print(sys.path)