from sys import stdin
input=lambda:stdin.readline().rstrip()

n=int(input())
x=[int(a) for a in input().split()]
p=1
minsum=10**8
for i in range(100):
    sum=0
    for j in range(n):
        sum+=(x[j]-p)**2
    minsum=min(minsum,sum)
    p+=1
print(minsum)