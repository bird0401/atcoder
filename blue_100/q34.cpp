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

    vector<int>dp(n);
    dp[0]=1;dp[1]=1;

    rrep(i,2,n+1) {
        dp[i]=dp[i-1]+dp[i-2];
    }

    cout<<dp[n]<<endl;
    return 0;
}