## 使用言語
- Python
- C++
- Java
- Rust
- Go

## 直近で知った気をつけること
- ２部グラフによるグラフ彩色は深さ優先探索を使う
- xy[x-1][y-1]=1;xy[y-1][x-1]=1
- from collections import defaultdict
- d=defaultdict(int)
- appendleftとappendを使い分けると高速化できる
- ナップザックは多次元になるとMLEの恐れがあるので１次元でpypyが良い
- infもっと多い場合もあるので注意

## 入出力

```
mod=10**9+7  
inf=10**9  
  
n=int(input())  
x=list(map(int, input().split()))  
n,m=map(int,input().split())  
c=[list(map(int, input().split())) for _ in range(n)] 
```

```
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int n;
    cin>>n;

    vector<int>x(n);
    rep(i,n) cin>>x[i];

    int h,w;
    cin>>h>>w;
    vector<vector<int>>x(h,vector<int>(w));
    rep(i,h) rep(j,w){
        cin>>x[i][j];
    }
    cout<<res<<endl;
    return 0;
}
```

```
struct st{
    int r,h,id;
};

bool cmp(st p,st q){
    if (p.r!=q.r) return p.r>q.r;
    else return p.h<q.h;
}
```

## 2人ゲームDP
```
dp[A][B]=0;
// dp[i][j] = Aからi個、Bからj個取った状態から最後までの先攻の最適スコア
for (int i=A;i>=0;i--) {
    for (int j=B;j>=0;j--) {
        if (i==A && j==B) continue;
        if ((i+j)%2==0){
            if (i==A) dp[i][j]=dp[i][j+1]+b[j];
            else if (j==B) dp[i][j]=dp[i+1][j]+a[i];
            else dp[i][j]=max(dp[i+1][j]+a[i],dp[i][j+1]+b[j]);
        }
        else{
            if (i==A) dp[i][j]=dp[i][j+1];
            else if (j==B) dp[i][j]=dp[i+1][j];
            else dp[i][j]=min(dp[i+1][j],dp[i][j+1]);
        }
    }
}
```

## nからk個を区別する場合の分け方

```
def n_same_k_different(n, k):
    ans = []
    if k == 1:
        return [[n]]
    for i in range(n+1):
        for j in n_same_k_different(n-i, k-1):
            ans.append([i]+j)
    return ans
```

## 分割数

```
dp = [[1]*(1001) for _ in range(1001)]
# dp[0][0]=1
for n in range(1,1001):
    for k in range(1001):
        if n-k>=0: dp[n][k] = (dp[n - 1][k - 1] + dp[n - k][k]) % mod
        else: dp[n][k] = dp[n - 1][k - 1]
```

## エラトステネスの篩
```
vector<int> Eratosthenes(int n){
    vector<int> is_prime(n+1,1);
    is_prime[0]=is_prime[1]=0;
    for(int i=2;i<n;i++){
        if(is_prime[i]==0) continue;
        for(int j=i*2;j<n;j+=i){
            is_prime[j]=0;
        }
    }
    return is_prime;
}
```
## ワーシャルフロイド
```
rep(k,10){rep(i,10){rep(j,10){c[i][j]=min(c[i][j],c[i][k]+c[k][j]);}}}
```

## 最大部分列和

```
currentsum,maxsum=-float("inf"),-float("inf")
for e in nums:
    currentsum=max(e,currentsum+e)
    maxsum=max(currentsum,maxsum)
return maxsum
```

## ソートの比較対象変更

```
sorted(s,key=lambda S:[x.index(c) for c in S])
```

## 部分和2つが対象、以上の場合

```
for i,(a,b) in enumerate(ab):
    for j in range(x+1):
        for k in range(y+1):
            dp[i+1][j][k]=min(dp[i][j][k],dp[i+1][j][k])
            dp[i+1][min(j+a,x)][min(k+b,y)]=min(dp[i+1][min(j+a,x)][min(k+b,y)],dp[i][j][k]+1)
```            

## LIS

```
import bisect
LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]
```        

```
sort(all(x));
vector<int>LIS(n,inf);
rep(i,n) *lower_bound(all(LIS),x[i].second)=x[i].second;
int res=find(all(LIS),inf)-LIS.begin();
```

左降順ソート、右についてLISを用いる。https://atcoder.jp/contests/joisc2016/tasks/joisc2016_a
```
for(i=0,j=0;i<q;i++) {
    for(;j<n;j++) {
        if (a[j].r<b[i].r) break;
        *upper_bound(all(LIS),a[j].h)=a[j].h;
    }
    res[b[i].id]=upper_bound(all(LIS),b[i].h)-LIS.begin();
}
```

## 隣接リスト
二人同士の関係性も管理可能

```
c=[[-1]*n for i in range(n)]
for i in range(m):
    x,y=map(lambda t:int(t)-1,input().split())
    c[x][y]=1;c[y][x]=1
for i in range(n):
    c[i][i]=1
```    

## 区間スケジューリング
大きい方の数を小さい順にソート→小さい順に残すものを選択

```
lr.sort(key=lambda t:t[1])
inf=10**9;pre,cnt=-inf,0
for e in lr:
    if pre<=e[0]:pre=e[1]
    else:cnt+=1
```    


## クラスカル法

```
V, E = map(int, input().split())
uf = UnionFind(V)

edges = []
for _ in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s, t))
edges.sort()

cost = 0
for edge in edges:
    w, s, t = edge
    if not uf.same(s, t):
        cost += w
        uf.union(s, t)
print(cost)
```

## 90度回転

```
list(zip(*s[::-1]))

## 尺取り法
ans,cur,cnt=0,0,0
for i in range(n):
    while cur<n:
        if d[a[cur]]==0 and cnt==k:break
        if d[a[cur]]==0:cnt+=1
        d[a[cur]]+=1;cur+=1
    ans=max(ans,cur-i)
    d[a[i]]-=1
    if d[a[i]]==0:cnt-=1
```

## 応用二分探索：最小の最大だったら最小xに結果がなるように計算してその結果が最大となるように決めていく

```
def f(m):
    cnt,st=0,0
    for e in a:
        if e-st>=m:cnt+=1;st=e
    if L-st<m:cnt=max(cnt-1,0)
    return True if cnt<k else False

inf=10**9
l,r=0,inf
while r-l>1:
    mid=(r+l)//2
    if f(mid):r=mid
    else:l=mid
print(l)
```

## 領域加算・２次元いもす法

```
hw=[[0]*1001 for _ in range(1001)]
for _ in range(n):
    lx,ly,rx,ry=map(int,input().split())
    hw[lx][ly]+=1
    hw[rx][ry]+=1
    hw[lx][ry]-=1
    hw[rx][ly]-=1
for i in range(1001):
    for j in range(1,1001):
        hw[i][j]+=hw[i][j-1]
for j in range(1001):
    for i in range(1,1001):
        hw[i][j]+=hw[i-1][j]
ba=[0]*(n+1)
for i in range(1001):
    for j in range(1001):
        ba[hw[i][j]]+=1
for i in range(1,n+1):
    print(ba[i])
```  

## 進数変換

```
print(bin(255))                 # 10進数 -> 2進数
print(hex(255))                 # 10進数 -> 16進数
print(int('0b11111111', 2))     # 2進数 -> 10進数
print(int('0xff', 16))          # 16進数 -> 10進数
```

## 回転

```
cos60,sin60=cos(radians(60)),sin(radians(60))
    af=[[cos60,-sin60],[sin60,cos60]]
```    
    
## 最長増加部分列

```
wh.sort(key=lambda t:(t[0],-t[1]))

from bisect import bisect_left
l=[]
for e in a:
    m=bisect_left(l,e)
    if m==len(l):l+=[e]
    else:l[m]=e
print(l)
```

## 個数制限付き部分和

```
dp=[[inf]*m for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(m):
        t=j+a[i]
        dp[i+1][t%m]=min(dp[i][t%m],dp[i][j]+t//m)
print("Yes" if dp[n][l]<=x else "No")
```

## 最長部分列

```
def lcs(s,t):
    n,m=len(s),len(t)
    dp=[0]*(m+1)
    for i in range(n):
        me=dp[:]
        for j in range(m):
            if s[i]==t[j]:dp[j+1]=me[j]+1
            elif dp[j+1]<dp[j]:dp[j+1]=dp[j]
    print(dp[m]) 
```    

## ナップザックdp

```
dp=[0]*(W+1)
for _ in range(n):
    v,w=map(int, input().split())
    for wei in range(W,w-1,-1):
        dp[wei]=max(dp[wei],dp[wei-w]+v)
print(dp[W])
```

## 個数制限なしナップザック

```
for _ in range(n):
    w,v=map(int, input().split())
    for wei in range(h+1):
        dp[min(wei+w,h)]=min(dp[min(wei+w,h)],dp[wei]+v)
print(dp[h])
```

## 素因数の数

```
ans,i=1,2
while i*i<=g:
    if g%i==0:
        ans+=1
        while g%i==0:g//=i
    i+=1
print(ans+(g>1))
```

##　素因数分解

```
def prime_fact(n):
    i=2
    primes=[]
    while n!=1:
        cnt=0
        while n%i==0:
            cnt+=1    
            n/=i
        primes.append([i,cnt])
        i+=1
    return primes
```

## 尺取法

```
s=l=ans=0
for r in range(n):
    s+=a[r]
    while s>=k:
        s-=a[l]
        l+=1
    ans+=l
```    

## 組み合わせ数

```
from math import factorial
def combination(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))
```    

## 順列列挙・辞書順探索

```
from itertools import permutations
per=sorted(set(permutations(sorted(s))))
```

```
do{
    string s;
    rep(i,k) s+=x[i];
    res.insert(s);
}while(next_permutation(x.begin(),x.end()));
```

## ビット全探索

```
for i in range(2**n):
    for j in range(n):
        if (i>>j)&1:
```        

## 約数の数

```
def prime(n):
    cnt=0
    for i in range(1,int(floor(sqrt(n)))+1):
        if n%i==0:
            cnt+=1
    return cnt*2
```    

## 約数列挙

```
def prime(n):
    ans=set()
    for i in range(1,int(floor(sqrt(n)))+1):
        if n%i==0:ans.add(i);ans.add(n//i)
    return ans
```    

## 行列積

```
exmat=[[[1,0,0],[0,1,0],[0,0,1]]]
def dot(a,b,c,m,r):
    if c==1:
        ans=[0]*r
        for j in range(r):
            for k in range(m):
                ans[j]+=a[k]*b[k][j]
    elif r==1:
        ans=[0]*c
        for j in range(c):
            for k in range(m):
                ans[j]+=a[j][k]*b[k]
    else:
        ans=[[0]*r for i in range(c)]
        for i in range(c):
            for j in range(r):
                for k in range(m):
                    ans[i][j]+=a[i][k]*b[k][j]
    return ans
    return ans
```    

## めぐる式二分探索

```
def isOK(index, key):
    if a[index] >= key: return True
    else: return False


def binary_search(key):
    ng,ok=-1,len(a)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, key): ok = mid
        else: ng = mid
    return ok
```    

## 数値降順ソート

```
desc = int(''.join(sorted(str(n), reverse = True)))
```

## ダイクストラ法

```
graph=[[] for _ in range(n)]
for i in range(n-1):
    a,b,d=map(int,input().split());a-=1;b-=1
    graph[a]+=[(b,d)]
    graph[b]+=[(a,d)]
from heapq import heappop,heappush
inf=10**9
def dijk(s):
    seen,dist=[False]*n,[inf]*n;dist[s]=0
    hq=[(dist[s],s)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]:continue
        seen[v]=True
        for to,cost in graph[v]:
            gcost=dist[v]+cost
            if gcost<dist[to]:
                dist[to]=gcost;heappush(hq,(gcost,to))
    return dist
```    

## 幅優先探索

```
from collections import deque
def bfs(si,sj,gi,gj):
    q=deque([(si,sj)])
    m=[[-1]*w for _ in range(h)]
    m[si][sj]=0
    while q:
        pi,pj=q.popleft()
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj=pi+i,pj+j
            if 0<=ni<h and 0<=nj<w and c[ni][nj]=='.':
                if m[ni][nj]<0:
                    m[ni][nj]=m[pi][pj]+1
                    q.append((ni,nj))
    return m[gi][gj]
```    

```
using Node=pair<int,int>;
deque<Node>q;
q.push_front(Node(si,sj));
vector<vector<int>> d={{-1,0},{1,0},{0,-1},{0,1}};
vector<vector<int>> dist(h,vector<int>(w,inf));dist[si][sj]=0;
while (!q.empty()){
    auto [pi,pj]=q.front();q.pop_front();
    rep(i,4){
        ni=pi+d[i][0];nj=pj+d[i][1];
        if (ni>=0 && ni<h && nj>=0 && nj<w){
            if (x[ni][nj]!='#'){
                if (dist[ni][nj]>dist[pi][pj]){
                    dist[ni][nj]=dist[pi][pj];
                    q.push_front(Node(ni,nj));
                }
            }
            else{
                if (dist[ni][nj]>dist[pi][pj]+1){
                    dist[ni][nj]=dist[pi][pj]+1;
                    q.push_back(Node(ni,nj));
                }
            }
        }
    }
}
```


## 深さ優先探索

```
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
from sys import setrecursionlimit
setrecursionlimit(10**7)
reached=[[False]*w for _ in range(h)]
def dfs(i,past):
    for v in graph[i]:
        if v==past:continue
        if not reached[v]:
            reached[v]=True
            dfs(v,i)
            reached[v]=False
```

## 深さ優先探索・順列

```
from collections import deque
def bfs(si,sj,goal):
    q=deque()
    q.append((si,sj))
    m=[[-1]*w for _ in range(h)]
    m[si][sj]=0
    while q:
        pi,pj=q.popleft()
        if c[pi][pj]==goal:return pi,pj,m[pi][pj]
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj=pi+i,pj+j
            if 0<=ni<h and 0<=nj<w and c[pi][pj]!='X' and m[ni][nj]<0:                
                m[ni][nj]=m[pi][pj]+1
                q.append((ni,nj))
```                

## Union-Find

```
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
 
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
 
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)
 
    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
 
    def flow(self, s, t):
        flow = 0
        f = INF = 10**9 + 7
        N = self.N
        while f:
            self.used = [0]*N
            f = self.dfs(s, t, INF)
            flow += f
        return flow
```
