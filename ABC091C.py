from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)]
cd=[list(map(int, input().split())) for _ in range(n)]

ab.sort(reverse=True)
cd.sort()
# print(ab)
searched=[False]*n
cnt=0
for i in range(n):
    miny=inf
    for j in range(n):
        if searched[j]==False and ab[i][0]<cd[j][0] and ab[i][1]<cd[j][1]<miny:
            miny=cd[j][1]
            cand=j
    if miny!=inf:
        # print("{} {}".format(ab[i],cd[cand]))
        searched[cand]=True
        cnt+=1
print(cnt)

