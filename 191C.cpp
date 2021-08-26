#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int judge(vector<string> &mass,int i,int j){
    if(mass.at(i).at(j)=='#') return 1;
    else return 0;
}

int dfs(int h,int w,vector<string> &mass){
    int cnt=0;
    rep(i,h-1) rep(j,w-1){
        if(mass.at(i).at(j)=='#'){
            bool t=false;
            if(judge(mass,i+1,j)+judge(mass,i-1,j)==2 && ) t=true;
            if(judge(mass,i,j+1)+judge(mass,i,j-1)==2) t=true;
            if(judge(mass,i+1,j+1)+judge(mass,i-1,j-1)==2) t=true;
            if(judge(mass,i-1,j+1)+judge(mass,i+1,j-1)==2) t=true;
            if(t==false)cnt++;
        }
    }
    return cnt;
}

int main(){
    int h,w;
    cin>>h>>w;
    vector<string> mass(h);
    rep(i,h) cin>>mass.at(i);
    vector<vector<int>> ex(h,vector<int>(w));
    cout<<dfs(h,w,mass)<<endl;
}