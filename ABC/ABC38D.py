from sys import stdin
from bisect import bisect_left

n=int(stdin.readline().rstrip())
boxes=[list(map(int,stdin.readline().split())) for _ in range(n)]

boxes.sort(key=lambda t:(t[0],-t[1]))
# print(boxes)
seq=list(map(lambda t:t[1],boxes))
LIS=[seq[0]]
for i in range(len(seq)):
    if seq[i]>LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect_left(LIS,seq[i])]=seq[i]
print(len(LIS))
