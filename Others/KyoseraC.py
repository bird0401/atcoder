n=int(input())
a=list(map(int, input().split()))
na=[e%200 for e in a]
ba=[0]*200
for e in na:
    ba[e]+=1
ans=0
for e in ba:
    ans+=e*(e-1)//2
print(ans)