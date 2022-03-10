n=int(input())
seq=[int(input()) for i in range(n)]

import bisect
LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
print(len(LIS))