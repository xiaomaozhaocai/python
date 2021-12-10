import os
# print([d for d in os.listdir('.')])
#
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])
#
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L if isinstance(s,str)])
#
# g = (x * x for x in range(10))
# for key in g:
#     print(key)

def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# for u7 in fib(17):
#     print(u7)

results = []
n = 0
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)