n=int(input())
graph=[[] for _ in range(n)]

nms=list(list(map(int,input().split())) for i in range(n))
nms.sort()
graph=[[]]
pre,j,cnt=nms[0][0],0,0
for i in range(n):
    if nms[i][0]==pre:graph[j]+=[nms[i][1]]
    else:j+=1;graph+=[[nms[i][1]]];pre=nms[i][0]
    
for i in range(j+1):
    graph[i]=set(graph[i])

for i in range(j+1):
    if len(graph[i])>=2:
        for k in range(j+1):
            lm=len(graph[i]&graph[k])
            if i!=k and lm>=2:cnt+=lm*(lm-1)//2
print(cnt//2)