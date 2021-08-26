from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

t=int(input())
for i in range(t):
    n,s,k=map(int,input().split())
    first=s
    cnt,ans=0,0
    while True:
        cnt=(n-s)//k
        ans+=cnt
        num=s+k*cnt
        if num==n:
            print(ans)
            break
        s=(num+k)%n
        ans+=1
        if s==first: 
            print(-1)
            break
        print(num)
        
# 4
# 10 4 3
# 1000 11 2
# 998244353 897581057 595591169
# 10000 6 14
# n,s,k,

# 2
# -1
# 249561088
# 3571

# 6+14n
# 6+14*713=9988,2
# 2+14n
# 2+14*714=9998,12
# 12+14n
# 12+14*713=9994,8



# (4+3n)%10=4,7,0,3,6,9,2,..
# (10-4)//3=2
# (11+2n)%1000=11,13,...,11+2*494=999,1,3,5,...
# (1000-11)//2=494

