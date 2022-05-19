#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

int main(){
    int n,q;
    cin>>n>>q;

    vector<int>x(q),y(q),z(q),w(q);
    rep(i,q) cin>>x[i]>>y[i]>>z[i]>>w[i];
    

    rep(i,60) rep(j,q) {
        w=(w[j]>>i)%2;
        if(w==0){
            bit[x[j]]=bit[y[j]]=bit[z[j]]=0;
        }else{
            bit[x[j]|bit[y[j]]|bit[z[j]]=0;
        }
    }

    cout<<res<<endl;
    return 0;
}

50


00000

50,32,0,13

110010
100000
000000
001101


4 2
1 2 3 50 110010
2 3 4 45 101101

1 2 3 4
0 0 0 1
1 0 0 0
0 0 0 1
