s,k=input().split()
k=int(k)
from itertools import permutations
per=sorted(set(permutations(sorted(s))))
print("".join(per[k-1]))
# print(per)