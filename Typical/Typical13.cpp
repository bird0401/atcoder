#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

ll N,M;
ll dist1[100009],distN[100009],dist[100009];
vector<pair<int,int>> G[100009];

void dijkstra(int st){
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> Q;
    rep(i,100009) dist[i]=inf;
    dist[st]=0;
    Q.push(make_pair(0,st));
    while (!Q.empty()) {
        int pos=Q.top().second;Q.pop();
        rep(i,G[pos].size()){
            int to=G[pos][i].first;
            ll cost=G[pos][i].second;
            if (dist[to]>dist[pos]+cost){
                dist[to]=dist[pos]+cost;
                Q.push(make_pair(dist[to],to));
            }
        }
    }
}

int main() {
    int a,b,c;
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
        cin>>a>>b>>c;
        G[a].push_back(make_pair(b, c));
		G[b].push_back(make_pair(a, c));
	}

	dijkstra(1);
	for (int i = 1; i <= N; i++) dist1[i] = dist[i];

	dijkstra(N);
	for (int i = 1; i <= N; i++) distN[i] = dist[i];

	for (int i = 1; i <= N; i++) {
		long long Answer = dist1[i] + distN[i];
		cout << Answer << endl;
	}
	return 0;
}