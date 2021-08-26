from sys import stdin
input=lambda:stdin.readline().rstrip()

n,x=map(int,input().split())
m=[int(input()) for _ in range(n)]
diff=x-sum(m)
min_m=min(m)
print(len(m)+int(diff//min_m))