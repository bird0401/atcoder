from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,k=map(int,input().split())
m=n%k
if -m+k<m:
    print(-m+k)
else:
    print(m)



# a-b -
# -a+b +
# -a+b-b=-a -
# a +