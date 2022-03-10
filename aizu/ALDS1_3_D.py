l,a,i=[],[],0
for s in input():
    if s=="\\":l+=[i]
    elif l and s=='/':
        j=l.pop()
        su=i-j
        while a and a[-1][0]>j:su+=a.pop()[1]
        a+=[(j,su)]
    i+=1
ans=[e for _,e in a]
print(sum(ans))
if a:print(len(ans),*ans)
else:print(0)