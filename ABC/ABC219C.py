x=input()
n=int(input())
s=[input() for i in range(n)]
s=sorted(s,key=lambda S:[x.index(c) for c in S])
for e in s:
    print(e)