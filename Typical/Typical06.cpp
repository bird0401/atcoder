#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rrep(i, m, n) for (int i = m; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;

int main(){
    int n,k;
    string s;
    cin>>n>>k>>s;
    
    int nex[s.size()+1][26];
    rep(i,26)nex[s.size()][i]=s.size();
    for(int i=s.size()-1;i>=0;i--){
        rep(j,26) {
            if ((int(s[i])-'a')==j) nex[i][j]=i;
            else nex[i][j]=nex[i+1][j];
        }
    }
    string res="";
    int current_pos=0;
    rrep(i,1,k+1) rep(j,26){
        int nex_pos=nex[current_pos][j];
        int possible_len=s.size()-nex_pos-1+i;
        if (possible_len>=k) {
            res+=(char)('a'+j);
            current_pos=nex_pos+1;
            break;
        }
    }
	cout << res << endl;
	return 0;
}   