from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
c=set([e//400 for e in a if e<3200])
n,m=len(c),sum([e>=3200 for e in a])
print("{} {}".format(max(1,n),n+m))