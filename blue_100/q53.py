import bisect

mod=10**9+7  
inf=10**10
  
n=int(input())
seq=[int(input()) for _ in range(n)] 
seq=seq[::-1] # 逆順にするとLISに帰着
LIS = [inf]*(n+1)
for i in range(n):
    LIS[bisect.bisect_right(LIS, seq[i])] = seq[i]
    # print(LIS)
print(bisect.bisect_left(LIS, inf))