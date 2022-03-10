from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

x,y=map(int,input().split())
if x>y:
    if x<y+3: print("Yes")
    else: print("No")
if y>x:
    if y<x+3: print("Yes")
    else: print("No")
