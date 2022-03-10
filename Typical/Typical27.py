n=int(input())
se=set()
for i in range(n):
    s=input()
    if s not in se:se.add(s);print(i+1)