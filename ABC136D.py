from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from copy import copy

s=input()
s+='R'
n,sr,br,ce,co,ans=len(s),0,-1,0,0,[]
for i in range(n):
    if s[i]=='L' and br==-1: br=i-1
    elif s[i]=='R' and br!=-1: 
        ans+=[0]*(br-sr)
        ans+=[[ce,co],[co,ce]][br%2!=0]
        ans+=[0]*(i-br-2)
        sr,br,ce,co=i,-1,0,0
    if i%2==0: ce+=1
    else: co+=1
for a in ans: print("{} ".format(a),end='')
print()