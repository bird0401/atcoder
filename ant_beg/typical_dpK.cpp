#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int n;
    cin>>n;
    vector<pair<int,int>> x(n);
    rep(i,n) {
        int a,b;
        cin>>a>>b;
        x[i]=make_pair(a+b,a-b);
    }
    sort(all(x));
    vector<int>LIS(n,inf);
    rep(i,n) *lower_bound(all(LIS),-x[i].second)=-x[i].second;
    int res=find(all(LIS),inf)-LIS.begin();
    cout<<res<<endl;
    return 0;
}