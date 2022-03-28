#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

// メモ化再帰 dp[l][r]で[l,r)でいくつ取り除けるか
string s;
int n;
vector<vector<int>> dp(301,vector<int>(301,-1));
int solve(int l,int r){
    int& res=dp[l][r];
    if ((r-l)<=2) {res=0;return 0;}
    if (res!=-1) return res;
    rrep(m,l+1,r){
        res=max(res,solve(l,m)+solve(m,r));
        if (s[l]=='i' && s[m]=='w' && s[r-1]=='i' 
        && solve(l+1,m)==m-(l+1) && solve(m+1,r-1)==(r-1)-(m+1)) res=r-l; //間の文字が全て取り除ける場合
    }
    return res;
}

int main(){
    cin>>s;
    int n = s.size();
    int res=solve(0,n)/3;
    // rep(i,n) {
    // rep(j,n) cout<<setw(2)<<dp[i][j]<<" ";
    // cout<<endl;
    // }
    cout<<res<<endl;
    return 0;
}