from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,m=map(int,input().split())
ab=[list(map(int, input().split())) for i in range(m)]
k=int(input())
cd=[list(map(int, input().split())) for i in range(k)]
maxcnt=0
for i in range(2**k):
    s=set()
    for j in range(k):
        if (i>>j)&1:
            s.add(cd[j][1])
        else:
            s.add(cd[j][0])
    cnt=0
    for j in range(m):
        if (ab[j][0] in s) and (ab[j][1] in s):
            cnt+=1
    maxcnt=max(maxcnt,cnt)
print(maxcnt)