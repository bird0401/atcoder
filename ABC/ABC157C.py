from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,m=map(int,input().split())
sc=[list(map(int, input().split())) for _ in range(m)]
for i in range(1000):
    st=str(i)
    if len(st)==n:
        for s,c in sc:
            if int(st[s-1])!=c: break
        else:
            print(st)
            exit()
print(-1)