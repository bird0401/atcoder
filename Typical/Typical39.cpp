#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// #define rep(i, n) for (int i = 0; i < (int)(n); i++)

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