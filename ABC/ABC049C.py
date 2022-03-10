from sys import stdin
input=lambda:stdin.readline().rstrip()

s=input()
s=''.join(list(reversed(s)))
l=["dream","dreamer","erase","eraser"]
for i in range(4):
    l[i]=''.join(list(reversed(l[i])))
# print(s[3])
i=0
while i<len(s):
    if s[i]=='m' and s[i:i+5]==l[0]:
        i+=5
    elif s[i]=='r' and s[i:i+7]==l[1]:
        i+=7
    elif s[i]=='r' and s[i:i+6]==l[3]:
        i+=6
    elif s[i]=='e' and s[i:i+5]==l[2]:
        i+=5
    else: 
        print("NO")
        exit()
print("YES")