n,k=map(int,input().split())
s=list(input());a=sorted(s)
import collections
ss,sa=collections.Counter(s),collections.Counter(s)
ans=""
for es in s:
    for ea in a:
        if es==ea:
            ss[es]-=1;sa[ea]-=1;ans+=ea;a.remove(ea);break
        else:
            k-=1;ss[es]-=1;sa[ea]-=1
            if sum(ss.values())-sum((ss&sa).values())<=k:
                ans+=ea;a.remove(ea);break
            else:k+=1;ss[es]+=1;sa[ea]+=1
print(ans)