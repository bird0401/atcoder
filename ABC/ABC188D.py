from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,C=map(int,input().split())
event=[]
for i in range(n):
    a,b,c=list(map(int, input().split()))
    event.append([a,c])
    event.append([b+1,-c])
event.sort()
pret,fee,ans=0,0,0
for t,c in event:
    ans+=(t-pret)*min(fee,C)
    fee+=c
    pret=t
print(ans)