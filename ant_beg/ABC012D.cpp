#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7
ll inf=1e9


int main(){
    int n,m;
    cin>>n>>m;

    int a,b,t;
    vector<vector<int>> d(n,vector<int>(n,inf));
    rep(i,n) d[i][i]=0;

    rep(i,m){
        cin>>a>>b>>t;
        d[a-1][b-1]=t;
        d[b-1][a-1]=t;

    }
    rep(k,n){
        rep(i,n){
            rep(j,n){
                d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
            }
        }
    }
    vector<int> maxd(n);
    rep(i,n){
        int temp=-1;
        rep(j,n){
            temp=max(temp,d[i][j]);
        }
        maxd[i]=temp;
    }
    int res=inf;
    rep(i,n){
        res=min(res,maxd[i]);
    }
    rep(i,n){rep(j,n){
        cout<<d[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<res<<endl;
    return 0;
}