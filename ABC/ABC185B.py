from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,m,t=map(int,input().split())
cap,preb=n,0
for i in range(m):
    a,b=map(int,input().split())
    n-=a-preb
    if n<=0: 
        print("No")
        exit()
    n,preb=min(n+b-a,cap),b
n-=t-preb
print(["No","Yes"][n>0])