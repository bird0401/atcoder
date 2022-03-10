n=int(input())
wh=[list(map(int, input().split())) for _ in range(n)]
wh.sort(key=lambda t:(t[0],-t[1]))
from bisect import bisect_left
l=[]
for w,e in wh:
        m=bisect_left(l,e)
        if m==len(l):l+=[e]
        else:l[m]=e
print(len(l))