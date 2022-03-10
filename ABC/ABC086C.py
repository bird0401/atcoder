from sys import stdin
input=lambda:stdin.readline().rstrip()

n=int(input())
points=[list(map(int,input().split())) for i in range(n)]
points=[[0,0,0]]+points
for i in range(1,n+1):
    diff_t=points[i][0]-points[i-1][0]
    diff_xy=abs(points[i][1]-points[i-1][1])+abs(points[i][2]-points[i-1][2])
    if diff_t-diff_xy<0 or (diff_t-diff_xy)%2==1:
        print("No")
        exit()
print("Yes")