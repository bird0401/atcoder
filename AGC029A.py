from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=input()
cnt,bcnt=0,0
for i in range(len(s)):
    if s[i]=='W':
        cnt+=bcnt
    else:
        bcnt+=1
print(cnt)