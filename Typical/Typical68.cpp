#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

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