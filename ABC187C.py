from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=set([input() for _ in range(n)])
for elem in s:
    if elem[0]!='!' and '!'+elem in s:
        print(elem)
        exit()
print("satisfiable")