from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=int(input())
nums=set([s])
while True:
    s=s/2 if s%2==0 else 3*s+1
    if s in nums: break
    else:
        nums.add(s)
print(len(nums)+1)

