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
  queue<tuple<int,int,int>>q;
  char x[1010][1010];
  rep(i,h){
    cin>>x[i];
    rep(j,w){
        if(x[i][j]=='#') q.emplace(i,j,0);
      }
  }
  int d[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
  int i,j,ni,nj,pi,pj,cnt;
  int res=-1;
  while(!q.empty()){
      tie(pi,pj,cnt)=q.front();q.pop();
      rep(k,4){
          i=d[k][0];j=d[k][1];
          ni=pi+i;nj=pj+j;res=max(res,cnt);
          if(ni>=0 and ni<h and nj>=0 and nj<w and x[ni][nj]=='.'){
             x[ni][nj]='#';
             q.emplace(ni,nj,cnt+1);
          }
      }
  }
  cout<<res<<endl;
  return 0;
}
