#include<bits/stdc++.h>
#define rep(i, n) for(long long i = 0; (i) < (long long)(n); (i)++)
using namespace std;
using ll = long long;

 int main(){
    ll inf=1e9;
    int h,w;
    cin>>h>>w;
    vector<vector<int>>c(10,vector<int>(10));
    rep(i,10){
        rep(j,10){
            cin>>c[i][j];
        }
    }
    rep(k,10){rep(i,10){rep(j,10){c[i][j]=min(c[i][j],c[i][k]+c[k][j]);}}}
    int res=0;
    int a;
    rep(i,h){
        rep(j,w){
            cin>>a;
            if(a!=-1){
                res+=c[a][1];
            }
        }
    }
    cout<<res<<endl;
    return 0;
 }
