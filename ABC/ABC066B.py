from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=input()
for i in range(len(s)-2,0,-2):
    if s[:i//2]==s[i//2:i]:
        print(i)
        exit()