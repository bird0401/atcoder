def merge(A,left,mid,right):
    inf=10**20
    a1,a2,i1,i2=A[left:mid]+[["",inf]],A[mid:right]+[["",inf]],0,0
    for i in range(left,right):
        if a1[i1][1]<=a2[i2][1]:A[i]=a1[i1];i1+=1
        else:A[i]=a2[i2];i2+=1

def merge_sort(A,left,right):
    if right-left>1:
        mid=(right+left)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid,right)
        merge(A,left,mid,right)

def partition(A,p,r):
    x=A[r][1]
    i1=p-1
    for i in range(p,r):
        if A[i][1]<=x:i1+=1;A[i1],A[i]=A[i],A[i1]
    i1+=1
    A[i1],A[r]=A[r],A[i1]
    return i1

def quicksort(A,p,r):
    if r-p>0:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

n=int(input())
sn,mn=[],[]
for _ in range(n):
    e1,e2=input().split()
    sn+=[[e1,int(e2)]]
    mn+=[[e1,int(e2)]]
# print(sn)
quicksort(sn,0,n-1)
merge_sort(mn,0,n)
print("Stable" if sn==mn else "Not stable")
for e in sn:
    print(*e)

        

