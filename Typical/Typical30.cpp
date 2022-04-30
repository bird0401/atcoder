#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
using namespace std;

int N, K;
int cnt[1 << 24];

int main() {
	// Step #1. Input
	cin >> N >> K;

	// Step #2. Count Number
	for (int i = 2; i <= N; i++) {
		if (cnt[i] >= 1) continue;
		for (int j = i; j <= N; j += i) cnt[j] += 1;
	}

    // rep(i,N+1) cout<<setw(2)<<i<<" ";
    // cout<<endl;
    // rep(i,N+1) cout<<setw(2)<<cnt[i]<<" ";
    // cout<<endl;

	// Step #3. Get Answer
	int Answer = 0;
	for (int i = 1; i <= N; i++) {
		if (cnt[i] >= K) Answer += 1;
	}
	cout << Answer << endl;
	return 0;
}