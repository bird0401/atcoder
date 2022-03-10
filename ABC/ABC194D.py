from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=0
for i in range(1,n):
    s+=1/float(n-i)
print(n*s)