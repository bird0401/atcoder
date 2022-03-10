from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
print(int((n//100+1)*100-n))
