a,b=map(int,input().split())
for i in range(b-a,0,-1):
    if (b//i-1)*i>=a:exit(print(i))