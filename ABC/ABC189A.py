from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=list(input())
if s[0]==s[1]==s[2]:
    print("Won")
else:
    print("Lost")