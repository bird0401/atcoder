n=int(input())
a=list(map(int, input().split()))
m,ans,ansl=min(n,8),[],[]
for i in range(2**m):
    s,l=0,[]
    for j in range(m):
        if i>>j&1:s+=a[j];l+=[j+1]
    ans+=[s%200];ansl+=[l]
an=len(ans)
for i in range(1,an):
    for j in range(1,an):
        if ans[i]==ans[j] and i!=j:
            print("Yes")
            print(len(ansl[i]),*ansl[i])
            print(len(ansl[j]),*ansl[j])
            exit()
print("No")