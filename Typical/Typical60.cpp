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

    vector<int>x(n);
    rep(i,n) cin>>x[i];

    vector<int> LIS1(n,inf),LIS2(n,inf);
    vector<int> P(n+1), Q(n+1);
    int res=-1;

    rep(i,n) {
        int pos=lower_bound(all(LIS1),x[i])-LIS1.begin();
        LIS1[pos]=x[i];
        P[i+1]=max(P[i],pos+1);
    }
    for(int i=n-1;i>-1;i--) {
        int pos=lower_bound(all(LIS2),x[i])-LIS2.begin();
        LIS2[pos]=x[i];
        Q[i+1]=max(Q[i],pos+1);
    }

    rrep(i,1,n+1) {
        res=max(res,P[i]+Q[i]-1);
    }

    cout<<res<<endl;
    return 0;
}

