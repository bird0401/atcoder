#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

vector<int> Eratosthenes(int n){
    vector<int> is_prime(n+1,1);
    is_prime[0]=is_prime[1]=0;
    for(int i=2;i<n;i++){
        if(is_prime[i]==0) continue;
        for(int j=i*2;j<n;j+=i){
            is_prime[j]=0;
        }
    }
    return is_prime;
}

int main(){
    vector<int> e=Eratosthenes(N);
    vector<int> c(N,0);
    for(int i=1;i<N;i++) c[i]=c[i-1]+(e[i] and e[(i+1)/2]);
    int q;
    cin>>q;
    int l,r;
    rep(i,q){
        cin>>l>>r;
        int res=c[r]-c[l-1];
        cout<<res<<endl;
    }
    return 0;
}
