n=int(input())
A=list(map(int, input().split()))
cnt=0

def merge(A,left,mid,right):
    inf=10**20
    a1,a2,i1,i2=A[left:mid]+[inf],A[mid:right]+[inf],0,0
    global cnt
    for i in range(left,right):
        if a1[i1]<a2[i2]:A[i]=a1[i1];i1+=1
        else:A[i]=a2[i2];i2+=1
        cnt+=1

def merge_sort(A,left,right):
    if right-left>1:
        mid=(right+left)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid,right)
        merge(A,left,mid,right)

merge_sort(A,0,n)
print(*A)
print(cnt)