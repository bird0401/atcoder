n,m=map(int,input().split())
ab=[list(map(int, input().split())) for i in range(m)]
ab.sort(key=lambda t:t[1]);pre,cnt=-1,0
for a,b in ab:
    if a>=pre:pre=b;cnt+=1
print(cnt)



