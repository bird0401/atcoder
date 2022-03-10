n=int(input())
r=[]
for i in range(n):
    x,l=map(int,input().split())
    r.append([x-l,x+l])
r.sort(key=lambda t:t[1])
inf=10**20
a,pre=0,-inf
for s,e in r:
    if s>=pre:
        a+=1
        pre=e
print(a)

