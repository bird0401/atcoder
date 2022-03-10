from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
cnt=0
while True:
    for i in range(n):
        if a[i]%2==0: a[i]/=2
        else: 
            print(cnt)
            exit()
    cnt+=1