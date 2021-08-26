from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=list(map(int, input().split()))
bac=[0]*(n+1)
for e in s: bac[e]+=1
sumb=sum([bac[i]*(bac[i]-1)//2 for i in range(n+1)])
for e in s: print(sumb-(bac[e]-1))