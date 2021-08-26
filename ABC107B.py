from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
import numpy as np

h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
a=[l for l in a if '#' in l]
a=np.array(a).T
a=[l for l in a if '#' in l]
a=np.array(a).T
for l in a: 
    ans="".join(l)
    print(ans)