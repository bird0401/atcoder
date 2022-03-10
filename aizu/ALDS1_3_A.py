x=list(input().split())
s=[]
for e in x:
    if e in "+-*":
        s2=s.pop()
        s1=s.pop()
        s+=[str(eval(s1+e+s2))]
    else:s+=[e]
print(s[0])