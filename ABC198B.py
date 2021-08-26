from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,s,ans=int(input()),input(),0
for i in range(1,n):
    a,b=set(s[:i]),set(s[i:])
    ans=max(ans,len(a&b))
print(ans)