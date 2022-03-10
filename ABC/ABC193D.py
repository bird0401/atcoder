from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

def score(a):
    s=0
    for i in range(9): s+=(10**a[i])*(i+1)
    return s

def judge(a,b):
    if score(a)>score(b): return True
    else: return False

k=int(input())
s=list(input())
t=list(input())
bs,bt=[0]*9,[0]*9
for i in range(4):
    bs[int(s[i])-1]+=1
    bt[int(t[i])-1]+=1
allcnt,wincnt=0,0
for i in range(9):
    if bs[i]+bt[i]==k: continue
    opi=k-bs[i]-bt[i]
    bs[i]+=1
    for j in range(9):
        if bs[j]+bt[j]==k: continue
        opj=k-bs[j]-bt[j]
        bt[j]+=1
        if judge(bs,bt):wincnt+=opi*opj
        allcnt+=opi*opj
        bt[j]-=1
    bs[i]-=1
print(float(wincnt)/allcnt)