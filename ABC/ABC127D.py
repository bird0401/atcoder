n,m=map(int,input().split())
a=list(map(int, input().split()))
bc=[list(map(int, input().split())) for _ in range(m)]
bc.sort(key=lambda t:-t[1])
for b,c in bc:
    a+=[c]*b
    if len(a)>=2*n:break
a.sort(reverse=True)
print(sum(a[:n]))