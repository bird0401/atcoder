s,t=input(),input()
n,m=len(s),len(t)
a=[]
for i in range(n-m+1):
    if s[i]=='?' or s[i]==t[0]:
        for j in range(m):
            if s[i+j]!='?' and s[i+j]!=t[j]:break
        else: a.append((s[:i]+t+s[i+m:]).replace('?','a'))
a.sort() 
print(a[0] if a else "UNRESTORABLE")