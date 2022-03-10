from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

k,n=map(int,input().split())
A=list(map(int, input().split()))
ans=A[0]+k-A[n-1]
for i in range(n-1):
    space=A[i+1]-A[i]
    ans=max(ans,space)
print(k-ans)
