#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main() {
    ll k;
    cin>>k;
    vector<ll> vec;
    for(ll i=1;i*i<=k;i++){
        if (k%i!=0) continue;
        vec.push_back(i);
        if (k/i!=i) vec.push_back(k/i);
    }
    sort(vec.begin(),vec.end());
    int res=0;
    rrep(i,0,vec.size()) rrep(j,i,vec.size()) {
        ll a=vec[i],b=vec[j],c=0;
        if (k/a<b) continue;
        if (k%(a*b)!=0) continue;
        c=k/(a*b);
        if (c>=b) res+=1;
    }
    cout<<res<<endl;
    return 0;
}