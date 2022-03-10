s=input()
n,su=len(s),0
for i in range(2**(n-1)):
    l=''
    for j in range(n):
        l+=s[j]
        if (i>>j)&1:l+='+'
    su+=eval(l)
print(su)