from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
L=list(map(int, input().split()))
cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a,b,c=L[i],L[j],L[k]
            if a!=b and b!=c and c!=a and a+b>c and b+c>a and c+a>b:
                cnt+=1
print(cnt)