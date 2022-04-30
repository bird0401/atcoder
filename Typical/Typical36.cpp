#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1<<18;

ll N, X[1 << 18], Y[1 << 18];
ll Q, T[1 << 18];
ll min_X = inf, max_X = -inf;
ll min_Y = inf, max_Y = - inf;

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