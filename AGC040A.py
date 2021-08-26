from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=input()
n=len(s)
ar=[0]*(n+1)
for i in range(n):
    if s[i]=='<': ar[i+1]=ar[i]+1
for i in range(n-1,-1,-1):
    if s[i]=='>': ar[i]=max(ar[i],ar[i+1]+1)
print(sum(ar))
