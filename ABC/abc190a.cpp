#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    int a,b,c;
    cin>>a>>b>>c;
    if(c==0){
        while(1){
            if(a==0) {
                cout<<"Aoki"<<endl;
                return 0;
            }
            a--;
            if(b==0) {
                cout<<"Takahashi"<<endl;
                return 0;
            }
            b--;
        }
    }else if(c==1){
        while(1){
            if(b==0) {
                cout<<"Takahashi"<<endl;
                return 0;
            }
            b--;
            if(a==0) {
                cout<<"Aoki"<<endl;
                return 0;
            }
            a--;
        }
    }
    
}