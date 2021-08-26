t,n=map(int,input().split())
l=[]
for i in range(1,101):
    l+=[i*(100+t)//100]
# print(l)
ansl=[]
for i in range(100-1):
    if l[i+1]!=l[i]+1:ansl+=[l[i]+1]
# print(ansl)
ans=(n-1)//t*(100+t)+ansl[(n-1)%t]
print(ans)

# 45
# pre,i=0,0
# while True:
#     p=i*(100+t)//100
#     if p==pre+2:pre=p;k=i;i+=1;break
#     pre=p;i+=1
# while True:
#     p=i*(100+t)//100
#     if p==pre+2:l=i;break
#     pre=p;i+=1
# ansi=(k-1)+(l-k)*(n-1)-1
# pre=ansi*(100+t)//100
# ansi+=1
# while True:
#     p=ansi*(100+t)//100
#     if p==pre+2:ans=pre+1;break
#     pre=p
#     ansi+=1
# print(ans)

# def judge(a):
#     p=a*100//(100+t)
#     if p*(100+t)//100!=a:return False
#     else return True

# 3 5

# 103/100 *34

# 1 1000000000
# 100, 201, 

# 33

# 50
# 1 3 5 7 

# 34 67 

2581114
3,6,9,12,