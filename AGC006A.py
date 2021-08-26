from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=input()
t=input()
for i in range(n):
    if s[i:]==t[:(n-i)]:
        print(len(s)+i)
        exit()
print(2*n)