s=input()
from collections import deque
q=deque([])
r=False
for e in s:
    if e=="R":r=not r
    elif r:q.appendleft(e)
    else:q.append(e)
if r:q.reverse()
ans,pre=[],-1
while q:
    e=q.popleft()
    if e!=pre:pre=e;ans+=[e]
    else:
        ans.pop()
        pre=ans[-1] if ans else -1
print(*ans,sep="")