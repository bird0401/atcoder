def partition(A,p,r):
    x=A[r]
    i1=p-1
    for i in range(p,r):
        if A[i]<=x:i1+=1;A[i1],A[i]=A[i],A[i1]
    i1+=1
    A[i1],A[r]=A[r],A[i1]
    return i1

n=int(input())
a=list(map(int, input().split()))
i1=partition(a,0,n-1)
print(*A[:i1],end="")
print(" [{}] ".format(A[i1]),end="")
print(*A[i1+1:])