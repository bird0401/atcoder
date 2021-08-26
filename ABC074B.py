from sys import stdin
input=lambda:stdin.readline().rstrip()

n=int(input())
k=int(input())
x=[int(a) for a in input().split()]
alldist=0
for i in range(n):
    if abs(x[i]-k)>abs(x[i]):
        alldist+=abs(x[i])
    else:
        alldist+=abs(x[i]-k)
print(alldist*2)