from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

a,b=map(str,input().split())
suma,sumb=sum(map(int,a)),sum(map(int,b))
if suma>=sumb: print(suma)
else: print(sumb)
