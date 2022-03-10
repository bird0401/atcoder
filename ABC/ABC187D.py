from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
diff,cnt=0,0
nab=[]
for i in range(n):
    a,b=map(int, input().split())
    diff+=a
    nab.append(a*2+b)
nab.sort(reverse=True)
for i in range(n):
    diff-=nab[i]
    cnt+=1
    if diff<0:
        print(cnt)
        exit()