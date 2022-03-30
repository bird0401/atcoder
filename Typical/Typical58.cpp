#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int digit_sum(int n){
    int sum=0;
    while(n!=0){
        sum+=n%10;n/=10;
    }
    return sum;
}

// 周期的に値が変化するのを用いる
int main(){
    ll n,k;
    cin>>n>>k;
    vector<int>nex(100000);
    rep(i,100000) {nex[i]+=(i+digit_sum(i))%100000;}

    vector<int> time_stamp(100000,-1);
    int cnt=0,pos=n;
    while(time_stamp[pos]==-1){
        time_stamp[pos]=cnt;
        pos=nex[pos];
        cnt++;
    }

    int cycle=cnt-time_stamp[pos];
    if (k>=cycle) k=(k-time_stamp[pos])%cycle+time_stamp[pos];

    int res;
    rep(i,100000) {if(time_stamp[i]==k) res=i;}
    cout<<res<<endl;
    return 0;
}