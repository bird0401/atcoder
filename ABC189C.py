from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
ua=list(set(a))
maxor=0
for i in range(len(ua)):
    num=ua[i]
    cnt,maxcnt=0,0
    for j in range(n):
        if a[j]>=num:
            cnt+=1
        else:
            maxcnt=max(maxcnt,cnt)
            cnt=0
    maxcnt=max(maxcnt,cnt)
    maxor=max(maxor,maxcnt*num)
print(maxor)