primes = []
i = 104723 
while(len(primes)<10001):
    indicator = 1
    for j in range(2,i//2):
        if i % j == 0:
            indicator = 0
    if indicator == 1:
        primes.append(i)
        print i, len(primes)
    i+=2