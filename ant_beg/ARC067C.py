mod=10**9+7  
from math import floor,sqrt
from collections import defaultdict

def prime_fact(n):
    i=2
    primes=[]
    while n!=1:
        cnt=0
        while n%i==0:
            cnt+=1    
            n/=i
        primes.append([i,cnt])
        i+=1
    return primes

n=int(input())  
all_prime=[0]*(n+1)
for i in range(1,n+1):
    pris=prime_fact(i)
    for prime,count in pris:
        all_prime[prime]+=count
sum=1
for count in all_prime:
    sum*=(count+1)
    sum%=mod
print(sum)