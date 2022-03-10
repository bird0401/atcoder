n,s,q=int(input()),list(input()),int(input())
fe=[s[:n],s[n:]]

for i in range(q):
    t,a,b=map(lambda t:int(t)-1,input().split())
    if t==0:fe[a//n][a%n],fe[b//n][b%n]=fe[b//n][b%n],fe[a//n][a%n]
    else: fe[0],fe[1]=fe[1],fe[0]
print(*(fe[0]+fe[1]),sep='')