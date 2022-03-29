// #include<bits/stdc++.h>
// using namespace std;
// #define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
// #define all(a)  (a).begin(),(a).end()
// ll mod=1e9+7;
// ll inf=1e9;
// ll N=101010;

// int main(){
//     int n;
//     cin>>n;

//     vector<int>x(n);
//     rep(i,n) cin>>x[i];

//     int h,w;
//     cin>>h>>w;
//     vector<vector<int>>x(h,vector<int>(w));
//     rep(i,h) rep(j,w){
//         cin>>x[i][j];
//     }
//     cout<<res<<endl;
//     return 0;
// }


#include<bits/stdc++.h>
using namespace std;
const int mod=1000000007;
int n,a,b,dp[1003],sz[1003],C[1003][1003],ans;
vector<int>v[1003];

void dfs(int x,int p){
	sz[x]=1;dp[x]=1;
    for(auto i:v[x]){
		if(i!=p){
			dfs(i,x);
			dp[x]=1ll*dp[x]*dp[i]%mod; //それぞれの部分木で何通りの書き方があるか
			sz[x]+=sz[i];
                // cout<<x<<" "<<i<<" "<<sz[i]<<" ";
                // cout<<endl;
            
		}
    }
    // cout<<x<<" "<<sz[x]<<endl;
	int nw=sz[x]-1;
    for (auto i:v[x]){
		if(i!=p){
			dp[x]=1ll*dp[x]*C[nw][sz[i]]%mod;
            cout<<nw<<" "<<sz[i]<<" "<<C[nw][sz[i]]<<endl;
			nw-=sz[i];
		}
    }
    cout<<endl;
}
int main(){
	cin>>n;
    // 二項係数を求める(n,k<=2000のとき有効)
	C[0][0]=1;
	for(int i=1;i<1003;i++){
		for(int j=0;j<1003;j++){
			C[i][j]=C[i-1][j];
			if(j)C[i][j]+=C[i-1][j-1];
			C[i][j]%=mod;
		}
    }
    // cout<<endl;
    // rep(i,10) {
    //     rep(j,10) cout<<setw(3)<<C[i][j]<<" ";
    //     cout<<endl;
    // }
	for(int i=1;i<n;i++){
		cin>>a>>b;
		a--;b--;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++) dp[j]=0,sz[j]=0;
		dfs(i,-1);
		ans=ans+dp[i]; ans%=mod;
        // cout<<dp[i]<<" ";
        // cout<<sz[i]<<endl;

	}
	// cout<<ans*500000004ll%mod<<endl;
    cout<<ans/2%mod<<endl;
    
}