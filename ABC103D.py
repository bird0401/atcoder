from sys import stdin

class AB:
    def __init__(self,a,b):
        self.a=a
        self.b=b

n,m=[int(x) for x in stdin.readline().split()]
ab=[]

for i in range(m):
    t1,t2=[int(x) for x in stdin.readline().rstrip().split()]
    ab.append(AB(t1,t2))

ab.sort(key=lambda t:t.b)
# for i in range(m):
#     print(ab[i].b)

cur=ab[0].b
cnt=1
for i in range(m):
    if cur<=ab[i].a:
        cur=ab[i].b
        cnt+=1
print(cnt)