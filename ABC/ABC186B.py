from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

h,w=map(int,input().split())
a=[list(map(int, input().split())) for _ in range(h)]
mina,suma=inf,0
for i in range(h):
    mina=min(mina,min(a[i]))
    suma+=sum(a[i])
print(suma-mina*h*w)