n,d,h=map(int,input().split())
t=0.0
for i in range(n):
    x,y=map(int,input().split())
    t=max(t,y-x*float(h-y)/(d-x))
print(t if t>0 else 0)