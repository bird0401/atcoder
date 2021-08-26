n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]
print(max([s.count(k)-t.count(k) for k in s]+[0]))