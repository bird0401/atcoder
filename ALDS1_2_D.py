n=int(input())
a=[int(input()) for _ in range(n)]
cnt=0
def insertion_sort(n,a,g):
    global cnt
    for i in range(g,n):
        v=a[i]
        j=i-g
        while j>=0 and a[j]>v:
            a[j+g]=a[j]
            j-=g
            cnt+=1
        a[j+g]=v

def shell_sort(a,n):
    g,pre=[1],4
    while pre<n:
        g+=[pre]
        pre=pre*3+1
    g=g[::-1]
    m=len(g)
    print(m)
    print(*g)
    for i in range(m):insertion_sort(n,a,g[i])
    print(cnt)
    for i in range(n):
        print(a[i])
shell_sort(a,n)