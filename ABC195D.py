from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,m,q=map(int,input().split())
wv=[list(map(int, input().split())) for _ in range(n)]
x=list(map(int, input().split()))
wv.sort(reverse=True,key=lambda t:t[1])
for i in range(q):
    l,r=map(int,input().split())
    nx=x[:l-1]+x[r:]
    nx.sort()
    val=0
    for w,v in wv:
        if len(nx)==0: break
        for j in range(len(nx)):
            if w<=nx[j]:
                del nx[j]
                val+=v
                break
    print(val)