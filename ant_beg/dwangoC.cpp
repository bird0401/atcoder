#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

list<int> n_same_k_different(int n,int k){
    list<int> ans;
    if (k == 1) return {{n}};
    rep(i,n+1){
        for(list<int> j:n_same_k_different(n-i, k-1)) {
            j.push_front(i);
            ans.insert(ans.end(),j.begin(),j.end());
        }
    }
    return ans;
}


int divide_combination(int n,int k){
    vector<vector<int>> dp(n+1,vector<int>(k+1));
    dp[0][0]=1;
    for(int i=1;i<n+1;i++) for(int j=1;j<k+1;j++) {
        if (j-k>=0) dp[i][j]=dp[i-1][j-1]+dp[i][j-k];
        else dp[i][j]=dp[i-1][j-1];
    }
    return dp[n][k];
}

int main(){
    int n,m;
    cin>>n>>m;

    // vector<int>a(n),b(m);
    // rep(i,n) cin>>a[i];
    // rep(i,m) cin>>b[i];

    for (auto i:n_same_k_different(n,m)) cout<<i<<" ";
    cout<<endl;
    // cout<<res<<endl;
    return 0;
}


// 4 1
// 3 2 1 0
// 5

// 4 4
// 2 1 1 1 4
// 1 1 1 1 5

// 0 0 0 4
// 0 0 1 3
// 0 0 2 2
// 0 1 1 2
// 1 1 1 1
// 4 0 0 0
// 3 0 0 1
// 2 0 0 2
// 2 0 1 1
// 1 0 0 3
// 1 0 1 2
