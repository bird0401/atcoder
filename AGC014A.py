from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

a,b,c=map(int,input().split())
cnt=0
if a==b==c and a%2==b%2==c%2==0:
    print(-1)
    exit()
while True:
    if a%2==1 or b%2==1 or c%2==1:
        break
    ta=a
    tb=b
    tc=c
    a=tb/2+tc/2
    b=tc/2+ta/2
    c=ta/2+tb/2
    cnt+=1
print(cnt)
    
    