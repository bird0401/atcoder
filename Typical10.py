n=int(input())
a,b,sa,sb=[0],[0],0,0
for i in range(n):
    c,p=map(int,input().split())
    if c==1:sa+=p;a+=[sa];b+=[sb]
    else:sb+=p;a+=[sa];b+=[sb]
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print("{} {}".format(a[r]-a[l-1],b[r]-b[l-1]))