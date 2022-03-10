#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    long long b,c;
    cin>>b>>c;
    long long n,min_e,max_e,min_o,max_o,d,ans;
    if(c>1){
        if(c%2==0){
        n=c/2;
        min_e=b-n;
        max_e=b+n-1;
        min_o=-b-n+1;
        max_o=-b+n-1;
        d=max(0LL,min(max_e,max_o)-max(min_e,min_o)+1);
        ans=(max_e-min_e+1)+(max_o-min_o+1)-d;
        }else{
            n=(c-1)/2;
            min_e=b-n;
            max_e=b+n-1;
            min_o=-b-n;
            max_o=-b+n;
            d=max(0LL,min(max_e,max_o)-max(min_e,min_o)+1);
            ans=(max_e-min_e+1)+(max_o-min_o+1)-d;
        }
    }else if(b!=0){
        ans=2;
    }else if(b==0){
        ans=1;
    }
    
    cout<<ans<<endl;
}
// b
// b-1
// -b
// -b
// ちょうど
// 奇数
// 2n+1
// n=0 -B
// -B-n ~ -B+n
// 2(n-1)+1
// -B-n+1 -B+n-1
// 偶数
// 2n
// n=0 B
// B-n ~ B+(n-1)

// 6
// 5
// 4
// 3