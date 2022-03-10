s=list(input());t=list(input());ans=[]
ls,lt=len(s),len(t)
for i in range(ls-lt+1):
    for j in range(lt):
        if s[i+j]!="?" and s[i+j]!=t[j]:break
    else:
        a=s[:i]+t+s[i+lt:]
        for i in range(len(s)):
            if a[i]=="?":a[i]="a"
        ans+=["".join(a)]
ans.sort()
print(ans[0] if len(ans)>0 else "UNRESTORABLE")  
