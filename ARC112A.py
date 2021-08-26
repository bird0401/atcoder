from sys import stdin

t=int(stdin.readline().rstrip())
for i in range(t):
    a,b=[int(x) for x in stdin.readline().rstrip().split()]
    if b-a>=a:
        sum=int((1+(b-2*a+1))*(b-2*a+1)/2)
        print(sum)
    else:
        print(0)
