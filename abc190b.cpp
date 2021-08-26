#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
struct M{
    int x;
    int y;
};

int main(){
    int n,s,d;
    cin>>n>>s>>d;
    vector<struct M> m(n);
    rep(i,n) cin>>m.at(i).x>>m.at(i).y;
    rep(i,n){
        if(m.at(i).x<s && m.at(i).y>d) {
            cout<<"Yes"<<endl;
            return 0;
        }
    }
    cout<<"No"<<endl;
}
