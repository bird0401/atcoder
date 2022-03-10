n=int(input())
a=list(map(int, input().split()))
b=[0]*3
for e in a:
    if e%4==0:b[2]+=1
    elif e%2==0:b[1]+=1
    else:b[0]+=1
print("Yes" if b[0]-b[2]<=(b[1]==0)  else "No")