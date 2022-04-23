#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

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