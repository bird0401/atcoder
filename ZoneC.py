n=int(input())
A=[list(map(int, input().split())) for _ in range(n)]

def f(x):
  s = set()
  for e in A:
    s.add(sum(1<<i for i in range(5) if e[i]>=x))
  for a in s:
    for b in s:
      for c in s:
        if(a|b|c == 0b11111):
          return True
  return False

inf=10**20
l,r=0,inf
while r-l>1:
    mid=(r+l)//2
    if f(mid):l=mid
    else:r=mid
print(l)