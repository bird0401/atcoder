from sys import stdin
input=lambda:stdin.readline().rstrip()

a,b=[int(x) for x in input().split()]
sum=1
cnt=0
while True:
    if sum>=b:
        break
    sum+=(a-1)
    cnt+=1
print(cnt)
