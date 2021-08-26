#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, n) for (int64_t i = 1; i <= (int64_t)(n); i++)

int main(){
    int64_t n;
    cin>>n;
    n*=2;
    int64_t cnt=0;
    // while(n%2==0)n/=2;
    int64_t sq=sqrt(n);
    rep2(i,sq){
        if(n%i==0){
            int64_t r=i;
            int64_t a=n/i;
            if((r+a)%2==1){
                cnt++;
            }
        }
    }
    cnt*=2;
    cout<<cnt<<endl;
}




// 12
// 12 12+12*1/2 24*1
// 3,4,5 (3+5)*(5-3+1)/2 8*3
// -2,-1,...,5 (-2+5)*(5-(-2)+1)/2 3*8
// -11,..,12 (12+(-11))*(12-(-11)+1)/2 1*24
// 1 3 6 10
// a,...,b (b+a)*(b-a+1)=2n
// 24 1*24 2*12 3*8 4*6 
// 2 2*1 1*2 

// 2n>=a+b>=1

// b>=a
// a>=1-b
// a<=2n-b
// a,b<=n


// b-a>=0

// x^2+x-2n=0
// -1+-sqrt(1-4*1*(-2))=-1+-sqrt(9)=1+-3
// 2
// x=2,-2=(b-a)