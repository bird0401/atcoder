n=int(input())
m=list(map(int, input().split()))
m.sort(reverse=True)
a=10**20
for i in range(n//m[0],-1,-1):
    n1=n-m[0]*i
    for j in range(n1//m[1],-1,-1):
        n2=n1-m[1]*j
        if n2%m[2]==0:a=min(a,i+j+n2//m[2])
print(a)