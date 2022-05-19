#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

int main(){
    int N,W;
    cin>>N>>W;

    vector<int>v(N),w(N);
    rep(i,N) cin>>v[i]>>w[i];

    vector<int> dp(W+1);
    rep(i,N) {
        for(int j=W;j>w[i]-1;j--){
            dp[j]=max(dp[j],dp[j-w[i]]+v[i]);
        }
    }
    for (auto& e:dp) cout<<e<<" ";
    cout<<endl;
    cout<<dp[W]<<endl;
    return 0;
}

