#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int H, W;
char c[20][20];
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };
bool used[20][20];

int dfs(int sx, int sy, int px, int py) {
	if (sx == px && sy == py && used[px][py]) return 0;
	used[px][py] = true;

	int ret = -10000;
	for (int i = 0; i < 4; i++) {
		int nx = px + dx[i], ny = py + dy[i];
		if (nx < 0 || ny < 0 || nx >= H || ny >= W || c[nx][ny] == '#') continue;
		if ((sx != nx || sy != ny) && used[nx][ny] == true) continue;
		int v = dfs(sx, sy, nx, ny);
		ret = max(ret, v + 1);
	}
	used[px][py] = false;
	return ret;
}

int main(){
    int res=-1;
    cin>>H>>W;
    rep(i,H) rep(j,W) cin>>c[i][j];
    rep(i,H) rep(j,W) res=max(res,dfs(i,j,i,j));

    if (res<=2) res=-1;
    cout<<res<<endl; 
    return 0;
}