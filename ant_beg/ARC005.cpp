#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int h,w;
    cin>>h>>w;
    vector<string>x(h);
    rep(i,h) {
        cin>>x[i];
    }
    int si,sj,gi,gj,ni,nj,pi,pj;
    rep(i,h) rep(j,w){
        if (x[i][j]=='s') {si=i;sj=j;}
        if (x[i][j]=='g') {gi=i;gj=j;} 
    }
    using Node=pair<int,int>;
    deque<Node>q;
    q.push_front(Node(si,sj));
    vector<vector<int>> d={{-1,0},{1,0},{0,-1},{0,1}};
    vector<vector<int>> dist(h,vector<int>(w,inf));dist[si][sj]=0;
    while (!q.empty()){
        auto [pi,pj]=q.front();q.pop_front();
        rep(i,4){
            ni=pi+d[i][0];nj=pj+d[i][1];
            if (ni>=0 && ni<h && nj>=0 && nj<w){
                if (x[ni][nj]!='#'){
                    if (dist[ni][nj]>dist[pi][pj]){
                        dist[ni][nj]=dist[pi][pj];
                        q.push_front(Node(ni,nj));
                    }
                }
                else{
                    if (dist[ni][nj]>dist[pi][pj]+1){
                        dist[ni][nj]=dist[pi][pj]+1;
                        q.push_back(Node(ni,nj));
                    }
                }
            }
        }
    }
    if (dist[gi][gj]<=2) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    return 0;
}
