#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int n,k;
    cin>>n>>k;
    vector<string>x(n);
    rep(i,n) cin>>x[i];
    sort(x.begin(),x.end());
    set<string> res;
    do{
        string s;
        rep(i,k) s+=x[i];
        res.insert(s);
    }while(next_permutation(x.begin(),x.end()));
    cout<<res.size()<<endl;
    return 0;
}
