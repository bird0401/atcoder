#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

struct st{
    int r,h,id;
};

bool cmp(st p,st q){
    if (p.r!=q.r) return p.r>q.r;
    else return p.h<q.h;
}

int main(){
    int n,q,r,h,i,j;
    cin>>n>>q;

    vector<st>a(n);
    rep(i,n) {
        cin>>r>>h;
        a[i].r=r;
        a[i].h=h;
    }
    sort(all(a),cmp);

    vector<st>b(q);
    rep(i,q) {
        cin>>r>>h;
        b[i].r=r;
        b[i].h=h;
        b[i].id=i;
    }
    sort(all(b),cmp);

    // cout<<endl;
    // rep(i,n) cout<<a[i].r<<","<<a[i].h<<endl;

    // cout<<endl;
    // rep(i,q) cout<<b[i].r<<","<<b[i].h<<endl;

    vector<int> LIS(n,inf),res(q);
    
    for(i=0,j=0;i<q;i++) {
        for(;j<n;j++) {
            if (a[j].r<b[i].r) break;
            *upper_bound(all(LIS),a[j].h)=a[j].h;
        }
        res[b[i].id]=upper_bound(all(LIS),b[i].h)-LIS.begin();
    }
    // rep(i,n) cout<<LIS[i]<<" ";
    // cout<<endl; 
    rep(i,q) cout<<res[i]<<endl;
    return 0;
}