s=[input() for i in range(3)]
t=list(input())
ans=[]
for e in t:
    ans+=s[int(e)-1]
print("".join(ans))