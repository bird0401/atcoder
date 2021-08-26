from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
n,m=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(n)]
x=list(map(int, input().split()))
exmat=[[[1,0,0],[0,1,0],[0,0,1]]]