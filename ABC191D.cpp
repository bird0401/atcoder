#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define ll long long
#define ld long double

int main(){
    ld a,b,c;
    cin>>a>>b>>c;
    ll x=round(a*10000), y=round(b*10000), r=round(c*10000);
    ll cnt=0;
    ll stx=ceil(double(x-r)/10000),enx=floor(double(x+r)/10000);
    // cout<<r<<endl;
    // r+=1e-7;
    // cout<<r<<endl;
    for(ll i=stx;i<=enx;i++){
        ld sq=sqrt(r*r-(x-i*10000)*(x-i*10000));
        ll aby=floor((y+sq)/10000);
        ll bey=ceil((y-sq)/10000);
        cnt+=aby-bey+1;
    }
    cout<<cnt<<endl;
}