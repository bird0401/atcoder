n=int(input())
a=list(map(int, input().split()))
q=int(input())
b=list(map(int, input().split()))
l=[]
for i in range(2**n):
    s=0
    for j in range(n):
        if (i>>j)&1:s+=a[j]
    l+=[s]
for e in b:
    if e in l:print("yes")
    else:print("no")