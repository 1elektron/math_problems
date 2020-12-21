n=600851475143 # the no to find prime factors of
primes=[]
i=2
while i<=n:
    if n%i==0:
        primes.append(i)
        n=n/i
    else:
        i=i+1
primes,set(primes)
