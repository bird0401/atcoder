s=input()
n=[]
for i in range(len(s)):
    if s[i]=='0': n+=['0']
    elif s[i]=='1': n+=['1']
    elif s[i]=='B' and len(n)!=0:n.pop(len(n)-1)
print(''.join(n))