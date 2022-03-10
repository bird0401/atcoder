n=int(input())
s=[list(input()) for _ in range(n)]
t=[list(input()) for _ in range(n)]
def limfind(c):
    flag=0
    for i in range(n):
        for j in range(n):
            if c[i][j]=="#":up=i;flag=1;break
        if flag==1:flag=0;break
    for j in range(n):
        for i in range(n):
            if c[i][j]=="#":ri=j;flag=1;break
        if flag==1:flag=0;break
    for i in range(n-1,-1,-1):
        for j in range(n):
            if c[i][j]=="#":do=i;flag=1;break
        if flag==1:flag=0;break
    for j in range(n-1,-1,-1):
        for i in range(n):
            if c[i][j]=="#":le=j;flag=1;break
        if flag==1:flag=0;break
    return up,ri,do,le

def con(a,b):
    i1,j1,i2,j2=limfind(a)
    k1,l1,k2,l2=limfind(b)
    if i1-i2==k1-k2 and j1-j2==l1-l2:
        flag,subi,subj=1,i1-k1,j1-l1
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                if a[i][j]!=b[i-subi][j-subj]:return False
        return True
    return False

for i in range(4):
    if con(s,t):print("Yes");exit()
    s=list(zip(*s[::-1]))
print("No")