from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

def dot(a,b,c,m,r):
    if c==1:
        ans=[0]*r
        for j in range(r):
            for k in range(m):
                ans[j]+=a[k]*b[k][j]
    else:
        ans=[[0]*r for i in range(c)]
        for i in range(c):
            for j in range(r):
                for k in range(m):
                    ans[i][j]+=a[i][k]*b[k][j]
    return ans

n=int(input())
xy1=[]
for i in range(n):
    x,y=map(int,input().split())
    xy1.append([[x],[y],[1]])

m=int(input())
exmat=[[[1,0,0],[0,1,0],[0,0,1]]]
for i in range(m):
    op=list(map(int, input().split()))
    if op[0]==1:
        c1=[[0,1,0],[-1,0,0],[0,0,1]]
        exmat.append(dot(c1,exmat[i],3,3,3))
    elif op[0]==2:
        c2=[[0,-1,0],[1,0,0],[0,0,1]]
        exmat.append(dot(c2,exmat[i],3,3,3))
    elif op[0]==3:
        c3=[[-1,0,2*op[1]],[0,1,0],[0,0,1]]
        exmat.append(dot(c3,exmat[i],3,3,3))
    elif op[0]==4:
        c4=[[1,0,0],[0,-1,2*op[1]],[0,0,1]]
        exmat.append(dot(c4,exmat[i],3,3,3))

q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    ans=dot(exmat[a],xy1[b-1],3,3,1)
    print("{} {}".format(ans[0][0],ans[1][0]))