#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(a)  (a).begin(),(a).end()
ll mod=1e9+7;
ll inf=1e9;
ll N=101010;

int main(){
    int A,B;
    cin>>A>>B;

    vector<int>a(A),b(B);
    rep(i,A) cin>>a[i];
    rep(i,B) cin>>b[i];
    vector<vector<int>> dp(A+1,vector<int>(B+1));
    dp[A][B]=0;
	// dp[i][j] = Aからi個、Bからj個取った状態から最後までの先攻の最適スコア
    for (int i=A;i>=0;i--) {
        for (int j=B;j>=0;j--) {
            if (i==A && j==B) continue;
            if ((i+j)%2==0){
                if (i==A) dp[i][j]=dp[i][j+1]+b[j];
                else if (j==B) dp[i][j]=dp[i+1][j]+a[i];
                else dp[i][j]=max(dp[i+1][j]+a[i],dp[i][j+1]+b[j]);
            }
            else{
                if (i==A) dp[i][j]=dp[i][j+1];
                else if (j==B) dp[i][j]=dp[i+1][j];
                else dp[i][j]=min(dp[i+1][j],dp[i][j+1]);
            }
        }
    }
    //         if ((i + j) % 2 == 0) {
    //             // 先攻番
    //             if (i == A) {
    //                 // Aの山が空
    //                 dp[i][j] = b[j] + dp[i][j + 1];
    //             }
    //             else if (j == B) {
    //                 // Bの山が空
    //                 dp[i][j] = a[i] + dp[i + 1][j];
    //             }
    //             else {
    //                 // 先攻は先攻スコアを最大化
    //                 dp[i][j] = max(a[i] + dp[i + 1][j], b[j] + dp[i][j + 1]);
    //             }
    //         }
    //         else {
    //             // 後攻番
    //             if (i == A) {
    //                 // Aの山が空
    //                 dp[i][j] = dp[i][j + 1];
    //             }
    //             else if (j == B) {
    //                 // Bの山が空
    //                 dp[i][j] = dp[i + 1][j];
    //             }
    //             else {
    //                 // 後攻は先攻スコアを最小化
    //                 dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]);
    //             }
    //         }
    //     }
    // }
    // cout<<endl;
    // rep(i, A + 1) {
    //     rep(j, B + 1) cout<<setw(2)<<dp[i][j]<<" ";
    //     cout<<endl;
    // }
    cout<<dp[0][0]<<endl;
    return 0;
}


// 5 5
// 2 4 5 4 2
// 2 8 3 4 5


// 8 3 4 5

// 2 5 2 8 4
// 4 4 2 3 5