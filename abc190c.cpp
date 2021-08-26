#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    int n,m,k;
    cin>>n>>m;
    vector<vector<int>> a(m,vector<int>(2));
    rep(i,m) cin>>a.at(i).at(0)>>a.at(i).at(1);
    cin>>k;
    vector<vector<int>> c(k,vector<int>(2));
    rep(i,k) cin>>c.at(i).at(0)>>c.at(i).at(1);
    int maxcnt=0;
    for (int tmp = 0; tmp < (1 << k); tmp++) {
        bitset<16> s(tmp);
        set<int> op;
        rep(i,k){
            if(s.test(i)) op.insert(c.at(i).at(1));
            else op.insert(c.at(i).at(0));
        }
        int cnt=0;
        rep(i,m){
            if(op.count(a.at(i).at(0))&&op.count(a.at(i).at(1)))cnt++;
        }
        maxcnt=max(maxcnt,cnt);
    }
    cout<<maxcnt<<endl;   
}

    // vector<int> bac(n+1);
    // rep(i,k)rep(j,2){
    //     bac.at(a.at(i).at(j))++;
    // }
    // rep(i,k){
    //     if(bac.at(c.at(i).at(0))>=bac.at(c.at(i).at(1)) && !op.count(c.at(i).at(0))) op.insert(c.at(i).at(0));
    //     else if(bac.at(c.at(i).at(0))<bac.at(c.at(i).at(1)) && !op.count(c.at(i).at(1))) op.insert(c.at(i).at(1));
    // }
    // int cnt=0;
    // rep(i,m){
    //     if(op.count(a.at(i).at(0))&&op.count(a.at(i).at(1)))cnt++;
    // }
    
// 6 12

// 2 3
// 4 6.
// 1 2.
// 4 5.
// 2 6.
// 1 5.
// 4 5.
// 1 3
// 1 2.
// 2 6.
// 2 3
// 2 5.

// 5
// 3 5
// 1 4
// 2 6
// 4 6
// 5 6

// 5
// 1
// 2
// 4
// 6

// 1 4
// 2 7
// 3 3
// 4 3
// 5 4
// 6 3
