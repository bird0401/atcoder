from sys import stdin
input=lambda:stdin.readline().rstrip()

n,a,b=map(int,input().split())
s=list(input())
cnta=0
cntb=0
for i in range(n):
    if(s[i]=='a'):
        if cnta+cntb<a+b:
            cnta+=1
            print("Yes")
        else:
            print("No")
    elif(s[i]=='b'):
        if cnta+cntb<a+b and cntb<b:
            cntb+=1
            print("Yes")
        else:
            print("No")
    elif(s[i]=='c'):
        print("No")

    

