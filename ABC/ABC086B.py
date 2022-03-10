from sys import stdin
input=lambda:stdin.readline().rstrip()

a,b=map(str,input().split())
num=int(a+b)
for i in range(400):
    if i*i==num:
        print("Yes")
        exit()
print("No")