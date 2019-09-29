sieve = [True] * 101
for i in range(2,100):
    if sieve[i]:
        print(i)
        for j in range(2,100):
            sieve[j] = False

# todo 
