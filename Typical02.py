n=int(input())
a=[]
for i in range(2**n):
    l,lc=[],0
    for j in range(n):
        if (i>>j)&1:l+=['('];lc+=1
        else:l+=[')'];lc-=1
        if lc<0:break
    if lc==0:a+=[l]
a.sort()
for e in a:
    print(*e,sep='')