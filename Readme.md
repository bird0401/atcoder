## 使用言語
- Python
- C++
- Rust
- Go

## 入出力

```
mod=10**9+7
inf=float('inf')
  
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
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

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
int N, M, a, b;
cin >> N >> M;
for (int i = 1; i <= M; i++) {
	cin >> a >> b;
	G[a].push_back(b);
	H[b].push_back(a);
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

## 転置
```
s=list(zip(*s))
```

## 2次元累積和
```
int main() {
	int N, K;
	cin >> N >> K;
	vector<int> A(N), B(N);
	for (int i = 0; i < N; ++i) {
		cin >> A[i] >> B[i];
	}

    int R = max(*max_element(A.begin(), A.end()), K);
	int C = max(*max_element(B.begin(), B.end()), K);
	vector<vector<int> > sum(R + 2, vector<int>(C + 2));

    // 行列の対応する(A,B)のマスに1を代入
	for (int i = 0; i < N; ++i) {
		++sum[A[i]][B[i]];
	}

    // for(int i=0;i<=R+1;i++){
    //     for(int j=0;j<=C+1;j++) cout<<sum[i][j]<<" ";
    //     cout<<endl;
    // }
    
    // 2次元累積和
	for (int i = 1; i <= R+1; ++i) {
		for (int j = 1; j <= C+1; ++j) {
			sum[i][j] += sum[i - 1][j];
		}
	}
	for (int i = 1; i <= R+1; ++i) {
		for (int j = 1; j <= C+1; ++j) {
			sum[i][j] += sum[i][j - 1];
		}
	}

    // 対応する範囲の人数を算出
	int answer = 0;
	for (int i = 1; i <= (R+1)-K; ++i) {
		for (int j = 1; j <= (C+1)-K; ++j) {
			answer = max(answer, sum[i-1][j-1] + sum[i+K][j+K] - sum[i-1][j+K] - sum[i+K][j-1]);
		}
	}

	cout << answer << endl;
	return 0;
}
```

## unionfind + 隅奇の法則性
```
class union_find {
private:
	int N;
	vector<int> par;
public:
	union_find() : N(0), par() {}
	union_find(int N_) : N(N_) {
		par.resize(N);
		for (int i = 0; i < N; ++i) {
			par[i] = i;
		}
	}
	int root(int x) {
		if (x == par[x]) return x;
		return par[x] = root(par[x]);
	}
	void link(int x, int y) {
		par[root(x)] = root(y);
	}
	bool connected(int x, int y) {
		return root(x) == root(y);
	}
};

int main() {
	int N, Q;
	cin >> N >> Q;
	vector<int> T(Q), X(Q), Y(Q), V(Q);
	for (int i = 0; i < Q; ++i) {
		cin >> T[i] >> X[i] >> Y[i] >> V[i];
		--X[i], --Y[i];
	}
	vector<int> sum(N - 1, 0);
	for (int i = 0; i < Q; ++i) {
		if (T[i] == 0) {
			sum[X[i]] = V[i];
		}
	}
    
    // rep(i,N) cout<<sum[i]<<" ";
    // cout<<endl;

    // A_x=0と仮定した時の現在わかっている全ての値
	vector<long long> potential(N, 0);
	for (int i = 0; i < N - 1; ++i) {
		potential[i + 1] = sum[i] - potential[i];
	}

    // rep(i,N) cout<<potential[i]<<" ";
    // cout<<endl;

	union_find uf(N);
	for (int i = 0; i < Q; ++i) {
		if (T[i] == 0) {
			uf.link(X[i], Y[i]);
		}
		if (T[i] == 1) {
            // union findでまだ連結していない場合はambiguous
			if (!uf.connected(X[i], Y[i])) {
				cout << "Ambiguous" << endl;
			}
            // 偶数同士、奇数同士のペアは片方が増えたらもう片方も増える
			else if ((X[i] + Y[i]) % 2 == 0) {
				cout << V[i] - potential[X[i]] + potential[Y[i]]<< endl;
			}
            // 偶奇が異なるペアは片方が増えたらもう片方は減る
			else {
				cout << -(V[i] - potential[X[i]]) + potential[Y[i]]<< endl;
			}
		}
	}
	return 0;
}
```

## c++で少数点桁数を指定した出力
```
cout<<fixed<<setprecision(15)<<res<<endl;
```

## 期待値の和による転倒数の期待値の算出
```
rep(i,N) rrep(j,i+1,N) { 
int num_invert=0,num_all=0;
rrep(k,L[i],R[i]+1) rrep(t,L[j],R[j]+1) {
    num_all++;
    if(k>t) num_invert++;
}
res+=double(num_invert)/num_all;
}
```

## 半分全列挙
```
long long N, K, P, Answer = 0;
long long A[100];
vector<long long> vec1[100], vec2[100];

int main() {
	cin >> N >> K >> P;
	for (int i = 0; i < N; i++) cin >> A[i];

	int mid = N / 2;
    // 前半
	for (int i = 0; i < (1 << mid); i++) {
		long long cnt1 = 0, cnt2 = 0;
		for (int j = 0; j < mid; j++) {
			if ((i & (1 << j)) != 0) { cnt1 += A[j]; cnt2 += 1; }
		}
		vec1[cnt2].push_back(cnt1);
	}
    // 後半
	for (int i = 0; i < (1 << (N - mid)); i++) {
		long long cnt1 = 0, cnt2 = 0;
		for (int j = 0; j < N - mid; j++) {
			if ((i & (1 << j)) != 0) { cnt1 += A[mid + j]; cnt2 += 1; }
		}
		vec2[cnt2].push_back(cnt1);
	}
	
	for (int i = 0; i <= N; i++) {
		sort(vec1[i].begin(), vec1[i].end());
		sort(vec2[i].begin(), vec2[i].end());
	}
	for (int h = 0; h <= K; h++) { // K以降の探索は不要
		for (int i = 0; i < (int)vec1[h].size(); i++) { 
            // P - vec1[h][i] + 1 以下の数がいくつあるか
			int pos1 = lower_bound(vec2[K - h].begin(), vec2[K - h].end(), P - vec1[h][i] + 1) - vec2[K - h].begin();
			Answer += (long long)pos1;
		}
	}

	cout << Answer << endl;
	return 0;
}
```

## 重複DP・それぞれの数に対する最小値
```
lim=10**6
dp=[inf]*lim # dp[i]: 正整数iを表すために必要な最小の正四面体数
dp[0]=0
dp_odd=[inf]*lim # 奇数のみ対象
dp_odd[0]=0

for n in range(1,10**2):
    w = n*(n+1)*(n+2)//6
    if w>=10**6: break
    for i in range(w,lim):
        v=dp[i-w]+1
        if dp[i]>v: dp[i]=v
```

## 条件付き列遷移最小値DP
```
dp=[[inf]*4 for _ in range(n+1)] # dp[i][j] i列目まで走査した時に、i列目がj色の時の最小値
for i in range(4): dp[0][i]=0

for i in range(1,n+1):
    for j in range(1,4):
        dp[i][j]=min(dp[i-1][k]+cost[i][j] for k in range(1,4) if j!=k)
# for e in dp: print(e)
print(min(dp[-1]))
```

## 日にち最小値DP
```
dp=[[inf]*(n+1) for _ in range(m+1)] # dp[i][j]:i日目に都市jにいるときのコストの最小値
for i in range(m+1):dp[i][0]=0

for i in range(1,m+1):
    for j in range(1,n+1):
        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1]+c[i-1]*d[j-1])

# for e in dp:print(e)
print(dp[m][n])
```

## 日にち最大値DP
```
dp=[[-inf]*m for _ in range(n+1)] #dp[i][j]: i日目にjの服を着る時の最大値
for i in range(1,n+1):
    for j in range(m):
        low,high,bri=c[j]
        if low<=t[i-1]<=high: 
            if i==1: dp[i][j]=0
            else: dp[i][j]=max(dp[i-1][k]+abs(bri-c[k][2]) for k in range(m))
# for e in dp: print(e)
print(max(dp[n]))
```

## 日にち連続条件dp
```
# dp[n][i][j]: iを一日前に食べjを二日前に食べているような、n日目までのパターン数
# 1,2日目前が存在しない場合に備え、パスタ0を入れておく。パスタ指定とパスタが連続にならないかのみを考えれば良いためこれで成り立つ
dp = [[[0]*4 for i in range(4)] for j in range(N+1)] 
dp[0][0][0] = 1

for n in range(1,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(1,4):
                if (A[n]==0 or A[n]==k) and (k != i or i != j): # パスタが指定されていないか指定のkと同じ場合で、三日連続ではない場合
                    dp[n][k][i] += dp[n-1][i][j]
                    dp[n][k][i] %= MOD
# for e in dp:
#     print(e)

ans = 0
for i in range(4): # 最終日、全ての状態の分を足す
    for j in range(4):
        ans += dp[-1][i][j]
        ans %= MOD
```

## 足し引きDP
```
n=int(input())
x=list(map(int, input().split()))
right=x[-1]
x=x[:n-1]
dp=[[0]*21 for _ in range(n-1)]; dp[0][x[0]]=1

for i in range(1,n-1):
    num=x[i]
    for j in range(21):
        if 0<=j-num<21: dp[i][j]+=dp[i-1][j-num]
        if 0<=j+num<21: dp[i][j]+=dp[i-1][j+num]

print(dp[-1][right])
```

## 区間DP・円環
```
N = int(input())
A = [int(input()) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)] #dp[i][[j]: A[i]からA[j]のケーキが残っている時のJOIの最大値
for i in range(N):
    for l in range(N):
        ln = (l+1)%N
        r = (l+i)%N
        rn = (r-1)%N
        if (N+i)%2: dp[l][r] = max(dp[ln][r]+A[l], dp[l][rn]+A[r]) # 左端のケーキと右端のケーキで大きい方
        else: dp[l][r] = dp[ln][r] if A[l]>A[r] else dp[l][rn] #A[l]の方が大きい場合はそちらを取るので、JOIはln~rの中から中から取る事になる

ans = max(dp[i][(i+N-1)%N] for i in range(N)) # 一周の仕方で値が変わるので注意。この中で最大値をansとする
# for e in dp: print(e)
print(ans)
```

## 区間DP
```
// メモ化再帰 dp[l][r]で[l,r)でいくつ取り除けるか
string s;
int n;
vector<vector<int>> dp(301,vector<int>(301,-1));
int solve(int l,int r){
    int& res=dp[l][r];
    if ((r-l)<=2) {res=0;return 0;}
    if (res!=-1) return res;
    rrep(m,l+1,r){
        res=max(res,solve(l,m)+solve(m,r));
        if (s[l]=='i' && s[m]=='w' && s[r-1]=='i' 
        && solve(l+1,m)==m-(l+1) && solve(m+1,r-1)==(r-1)-(m+1)) res=r-l; //間の文字が全て取り除ける場合
    }
    return res;
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

## 部分和2つが対象、以上の場合

```
for i,(a,b) in enumerate(ab):
    for j in range(x+1):
        for k in range(y+1):
            dp[i+1][j][k]=min(dp[i][j][k],dp[i+1][j][k])
            dp[i+1][min(j+a,x)][min(k+b,y)]=min(dp[i+1][min(j+a,x)][min(k+b,y)],dp[i][j][k]+1)
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

## 最長共通部分列DP

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

## 個数制限なしナップザックDP

```
dp=[0]*(W+1)  
for _ in range(N): 
    v,w=map(int, input().split())
    for wei in range(w,W+1):
        dp[wei]=max(dp[wei],dp[wei-w]+v)
print(dp[W])
```

## 共通部分列DP
```
x=list(input())
y=list(input())
nX,nY=len(x)+1,len(y)+1
dp = [[0]*nY for _ in range(nX)] 
for i in range(1,nX):
for j in range(1,nY):
    if x[i-1] == y[j-1]:
	dp[i][j] = dp[i-1][j-1] + 1
    else:
	dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
```    

## 巡回セールスマン・bitDP
```
V, E = map(int, input().split())
INF = 10**10
cost = [[INF]*V for _ in range(V)] # 重み
for e in range(E):
    s, t, d = map(int,input().split())
    cost[s][t] = d

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]

def dfs(S, v, dp):
    if dp[S][v] != -1: # 訪問済みならメモを返す
        return dp[S][v]
    if S==(1<<V)-1 and v==0: # 全ての頂点を訪れて頂点0に戻ってきた
        return 0 # もう動く必要はない

    res = INF
    for u in range(V):
        if S>>u & 1 == 0: # 未訪問かどうか
            res = min(res, dfs(S|1<<u, u, dp)+cost[v][u])
    dp[S][v] = res
    return res

ans = dfs(0, 0, dp) # 頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print (ans)
```

## bitDP・巡回セールスマン亜種
```
from sys import setrecursionlimit
INF =  float('inf')

setrecursionlimit(10**7)
N, M = map(int, input().split())
cost = [[[INF, 0] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s, t, d, time = map(int, input().split())
    cost[s-1][t-1] = [d, time]
    cost[t-1][s-1] = [d, time]

#dp[S][v]:= 集合Sを訪問済みで最後にvにいる場合の最短時間を第一引数に、その場合の数を第二引数にもつ
dp = [[[-1] * 2 for _ in range(N)] for _ in range(1<<N)]
dp[0][0]=[0, 1]

def dfs(S, v):
    if dp[S][v] != [-1, -1]:
        return dp[S][v]

    if S&(1<<v) == 0:
        dp[S][v] = [INF, 0]
        return dp[S][v]
    
    v_time = INF
    v_s = 0
    for prev in range(N):
        prev_time, prev_s = dfs(S^(1<<v), prev)
        if prev_time + cost[prev][v][0] > cost[prev][v][1]:continue
        if v_time > prev_time + cost[prev][v][0]:
            v_time = prev_time + cost[prev][v][0]
            v_s = prev_s
        elif v_time == prev_time + cost[prev][v][0]:
            v_s += prev_s
    
    dp[S][v] = [v_time, v_s]
    return dp[S][v]

ans1, ans2 = dfs((1<<N)-1, 0)
if ans1 == INF:
    print("IMPOSSIBLE")
else:
    print(ans1, ans2)
```

## 連鎖行列積問題・dp
```
INF = 10**10
N = int(input())
dp = [[INF]*N for _ in range(N)]
R = []
# 列数=行数でないと計算できない制約故に１次元で良い
for n in range(N):
    r, c = map(int,input().split())
    R.append(r)
R.append(c)

# print(R)

for i in range(N):
    dp[i][i] = 0 # 対角成分すなわち、行列積Miを計算するコストは0である

for l in range(1,N): # iとjの差分
    for i in range(N-l):
        j = i+l    
        for k in range(i,j):
            # cost(左側行列積) + cost(右側行列積) + 行列計算のコスト
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+R[i]*R[k+1]*R[j+1]) # 初回はR[0]*R[1]*R[2]
print (dp[0][-1])
```

## 木DP・部分木の数
```
void dfs(int pos, int pre) {
	long long val1 = 1, val2 = 1;
	for (int i : G[pos]) {
		if (i == pre) continue;
		dfs(i, pos);

		if (C[pos] == 'a') val1 *= (dp[i][0] + dp[i][2]); 
		if (C[pos] == 'b') val1 *= (dp[i][1] + dp[i][2]);
        val2 *= (dp[i][0] + dp[i][1] + 2LL * dp[i][2]);

		val1 %= mod;
		val2 %= mod;
	}

	if (C[pos] == 'a') dp[pos][0] = val1;
	if (C[pos] == 'b') dp[pos][1] = val1;

    dp[pos][2] = (val2 - val1 + mod) % mod;
}

int main() {
	// Step #1. Input
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> C[i];
	for (int i = 1; i <= N - 1; i++) {
		cin >> A[i] >> B[i];
		G[A[i]].push_back(B[i]);
		G[B[i]].push_back(A[i]);
	}

	// Step #2. DFS
	dfs(1, -1);
    // for(int i=1;i<N+1;i++) {
    //     for(int j=0;j<3;j++) cout<<dp[i][j]<<" ";
    //     cout<<endl;
    // }
	cout << dp[1][2] << endl;
	return 0;
}
```
## 木DP 主客転倒
```
long long N;
long long A[1 << 18], B[1 << 18];
long long dp[1 << 18];
vector<int> G[1 << 18];

void dfs(int pos, int pre) {
	dp[pos] = 1;
	for (int i : G[pos]) { // 直下の頂点
		if (i == pre) continue;
		dfs(i, pos);
		dp[pos] += dp[i]; // 木dp
	}
}

int main() {
	cin >> N;
	for (int i = 1; i <= N - 1; i++) {
		cin >> A[i] >> B[i];
		G[A[i]].push_back(B[i]);
		G[B[i]].push_back(A[i]);
	}

	dfs(1, -1);
    // rep(i,N+1) cout<<dp[i]<<" ";
    // cout<<endl<<endl;;
	long long Answer = 0;
	for (int i = 1; i <= N - 1; i++) {
        // cout<<dp[A[i]]<<" "<<dp[B[i]]<<endl;
		long long r = min(dp[A[i]], dp[B[i]]);
		Answer += r * (N - r);
	}
	cout << Answer << endl;
	return 0;
}
```

## RMQ
```
class RangeMax {
public:
	int size_ = 1;
	vector<long long> dat;

	void init(int sz) {
		while (size_ <= sz) size_ *= 2;
		dat.resize(size_ * 2, -(1LL << 60));
	}
	void update(int pos, long long x) {
		pos += size_;
		dat[pos] = x;
		while (pos >= 2) {
			pos >>= 1;
			dat[pos] = max(dat[pos * 2], dat[pos * 2 + 1]);
		}
	}
	long long query_(int l, int r, int a, int b, int u) {
		if (l <= a && b <= r) return dat[u];
		if (r <= a || b <= l) return -(1LL << 60);
		long long v1 = query_(l, r, a, (a + b) >> 1, u * 2);
		long long v2 = query_(l, r, (a + b) >> 1, b, u * 2 + 1);
		return max(v1, v2);
	}
	long long query(int l, int r) {
		return query_(l, r, 0, size_, 1);
	}
};
RangeMax Z[509];

long long W, N;
long long L[1 << 18], R[1 << 18], V[1 << 18];
long long dp[509][10009];

int main() {
	// Step #1. 入力
	cin >> W >> N;
	for (int i = 1; i <= N; i++) cin >> L[i] >> R[i] >> V[i];

	// Step #2. 初期化
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= W; j++) dp[i][j] = -(1LL << 60);
		Z[i].init(W + 2);
	}
	dp[0][0] = 0;
	Z[0].update(0, 0);

	// Step #3. 動的計画法
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j <= W; j++) dp[i][j] = dp[i - 1][j];
		for (int j = 0; j <= W; j++) {
			int cl = max(0, j - (int)R[i]), cr = max(0, j - (int)L[i] + 1); // 対象の範囲を求める
			if (cl == cr) continue;
			long long val = Z[i - 1].query(cl, cr); // 対象の範囲における価値のmax値を求める
			if (val != -(1LL << 60)) {
				dp[i][j] = max(dp[i][j], val + V[i]);
			}
		}
		for (int j = 0; j <= W; j++) Z[i].update(j, dp[i][j]); // 今回の結果を代入
	}

	// Step #4. 出力
	if (dp[N][W] == -(1LL << 60)) cout << "-1" << endl;
	else cout << dp[N][W] << endl;
	return 0;
}
```

## 遅延評価セグメント木
```
class segment_tree {
private:
	int sz;
	std::vector<int> seg;
	std::vector<int> lazy;
	void push(int k) {
		if (k < sz) {
			lazy[k * 2] = max(lazy[k * 2], lazy[k]);
			lazy[k * 2 + 1] = max(lazy[k * 2 + 1], lazy[k]);
		}
		seg[k] = max(seg[k], lazy[k]);
		lazy[k] = 0;
	}
	void update(int a, int b, int x, int k, int l, int r) {
		push(k);
		if (r <= a || b <= l) return;
		if (a <= l && r <= b) {
			lazy[k] = x;
			push(k);
			return;
		}
		update(a, b, x, k * 2, l, (l + r) >> 1);
		update(a, b, x, k * 2 + 1, (l + r) >> 1, r);
		seg[k] = max(seg[k * 2], seg[k * 2 + 1]);
	}
	int range_max(int a, int b, int k, int l, int r) {
		push(k);
		if (r <= a || b <= l) return 0;
		if (a <= l && r <= b) return seg[k];
		int lc = range_max(a, b, k * 2, l, (l + r) >> 1);
		int rc = range_max(a, b, k * 2 + 1, (l + r) >> 1, r);
		return max(lc, rc);
	}
public:
	segment_tree() : sz(0), seg(), lazy() {};
	segment_tree(int N) {
		sz = 1;
		while (sz < N) {
			sz *= 2;
		}
		seg = std::vector<int>(sz * 2, 0);
		lazy = std::vector<int>(sz * 2, 0);
	}
	void update(int l, int r, int x) {
		update(l, r, x, 1, 0, sz);
	}
	int range_max(int l, int r) {
		return range_max(l, r, 1, 0, sz);
	}
};
int main() {
	// cin.tie(0);
	// ios_base::sync_with_stdio(false);
	int W, N;
	cin >> W >> N;
	segment_tree seg(W);
	for (int i = 0; i < N; ++i) {
		int L, R;
		cin >> L >> R;
		int height = seg.range_max(L - 1, R) + 1;
		seg.update(L - 1, R, height);
		cout << height << '\n';
	}
	return 0;
}
```

## 座標圧縮
```
int W, N;
cin >> W >> N;
vector<int> L(N), R(N);
vector<int> compression;
for (int i = 0; i < N; ++i) {
	cin >> L[i] >> R[i];
	--L[i];
compression.push_back(L[i]);
	compression.push_back(R[i]);
}

sort(compression.begin(), compression.end());
compression.erase(unique(compression.begin(), compression.end()), compression.end()); //leave unique value

// for (auto& e:compression) cout<<e<<" ";
// cout<<endl;

for (int i = 0; i < N; ++i) {
	L[i] = lower_bound(compression.begin(), compression.end(), L[i]) - compression.begin();
	R[i] = lower_bound(compression.begin(), compression.end(), R[i]) - compression.begin();
// cout<<L[i]<<" "<<R[i]<<endl;
}
vector<int> h(compression.size() - 1);
for (int i = 0; i < N; ++i) {
	int height = *max_element(h.begin() + L[i], h.begin() + R[i]) + 1;
	fill(h.begin() + L[i], h.begin() + R[i], height);
	cout << height << '\n';
}
// for (auto& e:h) cout<<e<<" ";
// cout<<endl;
	
```

## 強連結成分分解（SCC）
```
bool used[100009];
vector<int> G[100009];
vector<int> H[100009];
vector<int> I;
long long cnts = 0;

void dfs(int pos) {
	used[pos] = true;
	for (int i : G[pos]) {
		if (!used[i]) dfs(i);
	}
	I.push_back(pos);
}

void dfs2(int pos) {
	used[pos] = true;
	cnts++;
	for (int i : H[pos]) {
		if (used[i] == false) dfs2(i);
	}
}

int main() {
	// Step #1. Input
    int N, M, a, b;
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
		cin >> a >> b;
		G[a].push_back(b);
		H[b].push_back(a);
	}

	// Step #2. First DFS
	for (int i = 1; i <= N; i++) {
		if (!used[i]) dfs(i);
	}

	// Step #3. Second DFS
	ll res = 0;
	reverse(I.begin(), I.end());
	for (int i = 1; i <= N; i++) used[i] = false;
	for (int i : I) {
		if (used[i] == true) continue;
		cnts = 0;
		dfs2(i);
		res += cnts * (cnts - 1LL) / 2LL;
	}

	// Step #4. Output The Answer!
	cout << res << endl;
	return 0;
}
```

## 前から貪欲法で前計算して、辞書順最小の部分文字列を抽出
```
    int nex[s.size()+1][26];
    rep(i,26)nex[s.size()][i]=s.size();
    for(int i=s.size()-1;i>=0;i--){
        rep(j,26) {
            if ((int(s[i])-'a')==j) nex[i][j]=i;
            else nex[i][j]=nex[i+1][j];
        }
    }
    string res="";
    int current_pos=0;
    rrep(i,1,k+1) rep(j,26){
        int nex_pos=nex[current_pos][j];
        int possible_len=s.size()-nex_pos-1+i;
        if (possible_len>=k) {
            res+=(char)('a'+j);
            current_pos=nex_pos+1;
            break;
        }
    }	
```

## DFSで出発地点と同じ場所の戻る時の最長距離を求める
```
int dfs(int sx, int sy, int px, int py) {
    cout<<sx<<" "<<sy<<" "<<px<<" "<<py<<endl;
	if (sx == px && sy == py && used[px][py]) return 0;
	used[px][py] = true;

	int ret = -10000;
	for (int i = 0; i < 4; i++) {
		int nx = px + dx[i], ny = py + dy[i];
		if (nx < 0 || ny < 0 || nx >= H || ny >= W || c[nx][ny] == '#') continue;
		if ((sx != nx || sy != ny) && used[nx][ny] == true) continue;
		int v = dfs(sx, sy, nx, ny);
		ret = max(ret, v + 1);
	}
	used[px][py] = false;
	return ret;
}
```

## 周期的に変化する値を求める
```
vector<int>nex(100000);
rep(i,100000) {nex[i]+=(i+digit_sum(i))%100000;}

vector<int> time_stamp(100000,-1);
int cnt=0,pos=n;
while(time_stamp[pos]==-1){
    time_stamp[pos]=cnt;
    pos=nex[pos];
    cnt++;
}

int cycle=cnt-time_stamp[pos];
if (k>=cycle) k=(k-time_stamp[pos])%cycle+time_stamp[pos];

int res;
rep(i,100000) {if(time_stamp[i]==k) res=i;}
```

## 全ての桁の和
```
int digit_sum(int n){
    int sum=0;
    while(n!=0){
        sum+=n%10;n/=10;
    }
    return sum;
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
for (int i = 1; i <= N; i++) {
	for (int j = 1; j <= N; j++) {
		if (A[i][j] == -1) dist[i][j] = lens;
		if (A[i][j] != -1) dist[i][j] = A[i][j];
	}
}
for (int k = 1; k <= N; k++) {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	}
}
```
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

## LIS・双対性

```
seq=seq[::-1] # 逆順にするとLISに帰着
LIS = [inf]*n
for i in range(n):
    LIS[bisect.bisect_right(LIS, seq[i])] = seq[i]
    # print(LIS)
print(bisect.bisect_left(LIS, inf))
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
vector<int> LIS(n,inf);
rep(i,n) *lower_bound(all(LIS),x[i])=x[i];
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

## 90度

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
long long get_border(long long cnts) {
	long long cl = 1, cr = 5000000000LL, cm, minx = 5000000000LL;
	for (int i = 0; i < 40; i++) {
		cm = (cl + cr) / 2LL;
		int res = count_number(cm);
		if (res <= cnts) { cr = cm; minx = min(minx, cm); } //res<=cntsの時のみminを保存することで境界の値を得る
		else { cl = cm; }
        // cout<<cl<<" "<<cm<<" "<<cr<<" "<<minx<<" "<<endl;
	}
	return minx;
}
```

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
vector<float> affine(float x, float y){
    float p[2]={x,y};
    int degree=45;
    float radian = degree * (M_PI / 180);
    float cos45=cos(radian),sin45=sin(radian);
    float af[2][2]={{cos45,-sin45},{sin45,cos45}};
    vector<float> res(2);
    rep(j,2) rep(k,2) {
        res[j]+=af[j][k]*p[k];
    }
    return res;
}
```

```
cos60,sin60=cos(radians(60)),sin(radians(60))
    af=[[cos60,-sin60],[sin60,cos60]]
```    

## マンハッタン距離最大

```
vector<ll> rotate45_manhattan(ll x,ll y){
    vector<ll> res(2);
    res[0]=x+y;
    res[1]=-x+y;
    return res;
}

int main() {
	cin >> N >> Q;

	rrep(i,1,N+1) cin >> X[i] >> Y[i];
	rrep(i,1,Q+1) cin >> T[i];

	rrep(i,1,N+1) {
        vector<ll> P(2);
        P = rotate45_manhattan(X[i],Y[i]);
        // for (auto& e:P) cout<<e<<" ";
        // cout<<endl;
		X[i] = P[0], Y[i] = P[1];
		min_X = min(min_X, X[i]);
		max_X = max(max_X, X[i]);
		min_Y = min(min_Y, Y[i]);
		max_Y = max(max_Y, Y[i]);
	}

	rrep(i,1,Q+1) {
		ll ret1 = abs(X[T[i]] - min_X);
		ll ret2 = abs(X[T[i]] - max_X);
		ll ret3 = abs(Y[T[i]] - min_Y);
		ll ret4 = abs(Y[T[i]] - max_Y);
		cout << max({ ret1, ret2, ret3, ret4 }) << endl;
	}
	return 0;
}
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

## ビット全探索・複数
```
long long bit_zentansaku() {
	long long ways = 0;
    // Nは今回の数列の数
	for (int i = 0; i < (1 << N); i++) {
		long long bit[15];
        // 今回のN個からなる数列の対象の桁のビットパターン
		for (int j = 0; j < N; j++) bit[j + 1] = (i / (1 << j)) % 2;

        // 全探索
		bool flag = true;
		for (int j = 1; j <= Q; j++) {
            if (((bit[X[j]] | bit[Y[j]]) | bit[Z[j]]) != w[j]) flag = false;
            
		}
		if (flag == true) ways++;
	}
	return ways;
}

int main() {
	// Step #1. Input
	cin >> N >> Q;
	for (int i = 1; i <= Q; i++) cin >> X[i] >> Y[i] >> Z[i] >> W[i];

	// Step #2. Brute Force
	long long Answer = 1;
	for (int i = 0; i < 60; i++) {
		for (int j = 1; j <= Q; j++) {
			w[j] = (W[j] / (1LL << i)) % 2LL; // 今回対象の桁のビット
		}
		long long ret = bit_zentansaku();
		Answer *= ret;
		Answer %= mod;
	}
	cout << Answer << endl;
	return 0;
}
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

## 素因数の種類数
```
for (int i = 2; i <= N; i++) {
	if (cnt[i] >= 1) continue;
	for (int j = i; j <= N; j += i) cnt[j] += 1;
}
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
void dijkstra(int st){
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> Q;
    rep(i,100009) dist[i]=inf;
    dist[st]=0;
    Q.push(make_pair(0,st));
    while (!Q.empty()) {
        int pos=Q.top().second;Q.pop();
        rep(i,G[pos].size()){
            int to=G[pos][i].first;
            ll cost=G[pos][i].second;
            if (dist[to]>dist[pos]+cost){
                dist[to]=dist[pos]+cost;
                Q.push(make_pair(dist[to],to));
            }
        }
    }
}
```

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
