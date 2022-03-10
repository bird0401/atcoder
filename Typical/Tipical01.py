n,l=map(int,input().split())
k=int(input())
a=list(map(int, input().split()))

def solve(M):
    cnt,pre=0,0
    for i in range(n):
        if a[i] - pre >= M and l - a[i] >= M:
            cnt+=1
            pre=a[i]
    if cnt>=k:return 1
    return -1
left,right=0,l
while right-left>1:
    mid=(right+left)//2
    if solve(mid)==-1:right=mid
    else:left=mid
print(left)