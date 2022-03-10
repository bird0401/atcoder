n,k=map(int,input().split())
a=list(map(int, input().split()))
from collections import defaultdict
d=defaultdict(int)
ans,cur,cnt=0,0,0
for i in range(n):
    while cur<n:
        if d[a[cur]]==0 and cnt==k:break
        if d[a[cur]]==0:cnt+=1
        d[a[cur]]+=1;cur+=1
    ans=max(ans,cur-i)
    d[a[i]]-=1
    if d[a[i]]==0:cnt-=1
print(ans)