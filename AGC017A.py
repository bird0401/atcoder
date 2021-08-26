n,p=map(int,input().split())
x=list(map(int, input().split()))
if sum([e%2 for e in x])==0:print(2**n if p==0 else 0)
else:print(2**(n-1))