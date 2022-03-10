from math import gcd,floor,sqrt
def prime(n):
    ans=set()
    for i in range(1,int(floor(sqrt(n)))+1):
        if n%i==0:ans.add(i);ans.add(n//i)
    return ans

n,m=map(int,input().split())
a=list(map(int, input().split()))
diss=set()
for i in range(n):
    diss|=prime(a[i])
diss.discard(1)
nums=set(range(1,m+1))
for i in diss:
    k=1
    while i*k<=m:
        nums.discard(i*k);k+=1
nums=list(nums);l=len(nums)
print(l)
for i in range(l):
    print(nums[i])