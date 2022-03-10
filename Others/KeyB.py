n=int(input())
lr=[]
for i in range(n):
    x,l=map(int,input().split())
    lr+=[[x-l,x+l]]
lr.sort(key=lambda t:t[1])
inf=10**20;pre,cnt=-inf,0
for e in lr:
    if pre<=e[0]:pre=e[1]
    else:cnt+=1
print(n-cnt)
