from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
tf=[input() for _ in range(n)]
ntf=[1 if x=="OR" else 0 for x in tf]

def counttf(p):
    if p==0 and ntf[0]==0:
        return 1
    elif p==0 and ntf[0]==1:
        return 3
    if ntf[p]==0:
        return counttf(p-1)
    else:
        return 2**(p+1)+counttf(p-1)

print(counttf(len(ntf)-1))