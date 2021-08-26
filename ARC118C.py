n=int(input())
l=set([6,10,15])
for i in [6,10,15]:
    j=1
    while i*j<=10000:
        l.add(i*j)
        j+=1
print(*list(l)[:n])