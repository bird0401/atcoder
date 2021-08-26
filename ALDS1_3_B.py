from collections import deque
n,q=map(int,input().split())
nt=deque((input().split() for _ in range(n)))
st=0
while nt:
    na,t=nt.popleft()
    t=int(t)
    st+=min(t,q)
    if t<=q:print("{} {}".format(na,st))
    else:nt+=[[na,str(t-q)]]