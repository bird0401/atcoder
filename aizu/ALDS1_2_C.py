n=int(input())
x=list(map(lambda t:[t[0],int(t[1])],input().split()))

def bubble_sort(n,a):
    flag=1
    while flag:
        flag=0
        for j in range(n-1,0,-1):
            if a[j-1][1]>a[j][1]:
                t=a[j]
                a[j]=a[j-1]
                a[j-1]=t
                flag=1
    b=[a[i][0]+str(a[i][1]) for i in range(n)]
    print(*b)
    return a

def selection_sort(n,a):
    for i in range(n):
        minj=i
        for j in range(i,n):
            if a[j][1]<a[minj][1]:minj=j
        t=a[i]
        a[i]=a[minj]
        a[minj]=t
    b=[a[i][0]+str(a[i][1]) for i in range(n)]
    print(*b)
    return a

def issta(n,a,b):
    for i in range(n-1):
        if b[i][1]==b[i+1][1]:
            pre,pos=b[i],b[i+1]
            flag=0
            for j in range(n):
                if a[j]==pre:flag=1
                if a[j]==pos:
                    if flag:break
                    else:exit(print("Not stable"))
    print("Stable")

from copy import deepcopy
a1=deepcopy(x)
bubble_sort(n,a1)
issta(n,x,a1)
a2=deepcopy(x)                
selection_sort(n,a2)
issta(n,x,a2)
