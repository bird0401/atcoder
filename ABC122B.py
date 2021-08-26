from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=list(input())
maxcnt,cnt=0,0
for i in range(len(s)):
    if "ACGT".count(s[i])==1:
        cnt+=1
        maxcnt=max(maxcnt,cnt)
    else:
        cnt=0
print(maxcnt)