from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=input()
ans=inf
for i in range(len(s)-2):
    ans=min(ans,abs(753-int(s[i:i+3])))
print(ans)