#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;


int main() {
	int N;
	cin >> N;
	vector<int> L(N), R(N);
    double res=0.0;

	for (int i = 0; i < N; ++i) {
		cin >> L[i] >> R[i];
	}

    rep(i,N) rrep(j,i+1,N) { 
        int num_invert=0,num_all=0;
        rrep(k,L[i],R[i]+1) rrep(t,L[j],R[j]+1) {
            num_all++;
            if(k>t) num_invert++;
        }
        res+=double(num_invert)/num_all;
    }

    cout<<fixed<<setprecision(15)<<res<<endl;

	return 0;
}