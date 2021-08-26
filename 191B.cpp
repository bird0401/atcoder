#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    int n,x;
    cin>>n>>x;
    vector<int> a(n);
    int temp;
    int cnt=0;
    rep(i,n) {
        cin>>temp;
        if(temp!=x) {
            a.at(cnt)=temp; cnt++;
        }
    }
    rep(i,cnt) cout<<a.at(i)<<" ";
    cout<<endl;
}