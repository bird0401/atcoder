from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

x=str(input())
dotidx=x.find('.')
x=x[:dotidx] if dotidx!=-1 else x
print(int(x))