from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

a,b,c=map(int,input().split())
if a>b:
    print("Takahashi")
elif a<b:
    print("Aoki")
elif a==b:
    if c==0:
        print("Aoki")
    else:
        print("Takahashi")
    
