from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,x=map(int,input().split())
a=list(map(int, input().split()))
a.sort()
for i in range(n):
    if x>a[i]:x-=a[i]
    elif x==a[i]:
        print(i+1)
        exit()
    else:
        print(i)
        exit()
print(n-1)