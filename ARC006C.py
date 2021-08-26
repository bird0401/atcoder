from sys import stdin
input=lambda:stdin.readline().rstrip()

n=int(input())
weights=[int(input()) for _ in range(n)]
piles=[]
for w in weights:
    for p in piles:
        if p[-1]>=w:
            p+=[w]
            break
    else:
        piles+=[[w]]
print(len(piles))