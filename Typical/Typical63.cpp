#include<bits/stdc++.h>
// #include <iostream>
// #include <vector>
// #include <map>
// #include <algorithm>

using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int maximum_same(vector<int> R) {
    int res=0;
    map<int,int> num_cnt;
    for (auto e : R){
        num_cnt[e]++;
        res=max(num_cnt[e],res);
    }
    return res;
}

int main(){
    int H,W;
    int res=-1;
    cin>>H>>W;
    vector<vector<int>>P(H,vector<int>(W));
    rep(i,H) rep(j,W){
        cin>>P[i][j];
    }

    rep(i,(1<<H)){
        vector<int> R;
        rep(j,W){
            bool flag=false;int idx=-1;
            rep(k,H){
                if((i&(1<<k))==0) continue;
                if (idx==-1) idx=P[k][j];
                else if (P[k][j]!=idx) {flag=true;break;}
            }
            if (!flag) R.push_back(idx);
        }

        int cntH=0,cntW=maximum_same(R);
        rep(j,H) {
            if ((i&(1<<j))!=0) cntH++;
        }
        
        res=max(res,cntH*cntW);
    }
    cout<<res<<endl;
    return 0;
}
