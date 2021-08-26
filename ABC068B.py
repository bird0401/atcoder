from sys import stdin
input=lambda:stdin.readline().rstrip()

n=int(input())
a=1
while a<=n:
    a*=2
print(a//2)