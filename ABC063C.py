from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=[int(input()) for _ in range(n)]
s+=[0]
s.sort()
ans=sum(s)
for e in s:
    if (ans-e)%10!=0:
        print(ans-e)
        exit()
else: print(0)