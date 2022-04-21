#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int N;
    cin>>N;

    vector<long>X(N),Y(N);
    rep(i,N) cin>>X[i]>>Y[i];
    sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());
    long midx=X[N/2],midy=Y[N/2],sumx=0,sumy=0;
    rep(i,N) sumx+=abs(X[i]-midx);
    rep(i,N) sumy+=abs(Y[i]-midy);
    cout<<sumx+sumy<<endl;
    return 0;
}