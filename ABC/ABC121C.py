from sys import stdin
input=lambda:stdin.readline().rstrip()

n,m,c=map(int,input().split())
B=list(map(int,input().split()))
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
# print(B)
# print(A)
cnt=0
for i in range(n):
    sum=0
    for j in range(m):
        sum+=(B[j]*A[i][j])
    sum+=c
    if int(sum)>0:
        cnt+=1
print(int(cnt))
