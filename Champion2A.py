x,y,z=map(int,input().split())
for i in range(1000000,-1,-1):
    if y/x>i/z:exit(print(i))