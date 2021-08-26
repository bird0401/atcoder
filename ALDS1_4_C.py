n=int(input())
s=set()
for i in range(n):
    x=list(input().split())
    if x[0]=="insert":s.add(x[1])
    else:print(["no","yes"][x[1] in s])