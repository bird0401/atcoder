#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int n;
    cin>>n;

    vector<int>x(n);
    rep(i,n) cin>>x[i];

    vector<bool> dp(10001,false);dp[0]=true;
    rep(i,n){
        int k=x[i];
        for(int j=10001;j>=0;j--) if(dp[j]) dp[j+k]=true;
    }
    int res=0;
    rep(i,10001) res+=dp[i];
    cout<<res<<endl;
    return 0;
}