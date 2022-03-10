from sys import stdin
input=lambda:stdin.readline().rstrip()

A=[]
for i in range(3):
    A.append([int(x) for x in input().split()])

n=int(input())
for i in range(n):
    b=int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k]==b:
                A[j][k]=0
for i in range(3):
    t=True
    for j in range(3):
        if A[i][j]!=0:
            t=False
            break
    if t==True:
        print("Yes")
        exit()
for i in range(3):
    t=True
    for j in range(3):
        if A[j][i]!=0:
            t=False
            break
    if t==True:
        print("Yes")
        exit()
j=0
k=0
for i in range(3):
    t=True
    if A[j][k]!=0:
        t=False
        break
    j+=1
    k+=1
if t==True:
    print("Yes")
    exit()
j=2
k=0
for i in range(3):
    t=True
    if A[j][k]!=0:
        t=False
        break
    j-=1
    k+=1
if t==True:
    print("Yes")
    exit()
print("No")
# print(A)