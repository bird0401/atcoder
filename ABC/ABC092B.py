from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
d,x=map(int,input().split())
cnt=0
for i in range(n):
    a=int(input())
    cnt+=1+(d-1)//a
print(cnt+x)