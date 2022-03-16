#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7;
ll inf=1e9;

// vector<int> Eratosthenes(int n){
//     vector<int> is_prime(n+1,1);
//     is_prime[0]=is_prime[1]=0;
//     for(int i=2;i<n;i++){
//         if(is_prime[i]==0) continue;
//         for(int j=i*2;j<n;j+=i){
//             is_prime[j]=0;
//         }
//     }
    // rep(i,20) cout<<is_prime[i]<<" ";
    // cout<<endl;
//     return is_prime;
// }

vector<bool> Eratosthenes(int N) {
    // テーブル
    vector<bool> isprime(N+1, true);

    // 0, 1 は予めふるい落としておく
    isprime[0] = isprime[1] = false;

    // ふるい
    for (int p = 2; p <= N; ++p) {
        // すでに合成数であるものはスキップする
        if (!isprime[p]) continue;

        // p 以外の p の倍数から素数ラベルを剥奪
        for (int q = p * 2; q <= N; q += p) {
            isprime[q] = false;
        }
    }
    rep(i,20) cout<<isprime[i]<<" ";
    cout<<endl;

    // 1 以上 N 以下の整数が素数かどうか
    return isprime;
}

int main(){
    vector<bool> e=Eratosthenes(10010);
    // vector<int> c(10^5+10,0);
    // rep(i,10^5) c[i+1]=c[i]+e[i];
    // int q;
    // cin>>q;
    // int l,r,res;
    // rep(i,q){
    //     cin>>l>>r;
    //     res+=c[r]-c[l-1];
    // }
    // rep(i,10) cout<<c[i]<<" "; 
    // cout<<res<<endl;
    return 0;
}
