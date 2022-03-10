from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

def culc(n):
    n1=int(''.join(sorted(list(str(n)))))
    n2=int(''.join(sorted(list(str(n)),reverse=True)))
    return n2-n1
n,k=map(int,input().split())
for i in range(k):
    n=culc(n)
print(n)