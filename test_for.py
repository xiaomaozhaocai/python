alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append(i*i)

print(alist)

blist = [i*i for i in range(1,11) if (i%2) == 0]
print(blist)

clist = [j*j for j in range(1,11) if (j%2) == 0]


z_num = {i:0 for i in range(1,11)}
print(z_num)