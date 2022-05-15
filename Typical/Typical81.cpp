#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int N, K;
	cin >> N >> K;
	vector<int> A(N), B(N);
	for (int i = 0; i < N; ++i) {
		cin >> A[i] >> B[i];
	}

    int R = max(*max_element(A.begin(), A.end()), K);
	int C = max(*max_element(B.begin(), B.end()), K);
	vector<vector<int> > sum(R + 2, vector<int>(C + 2));

    // 行列の対応する(A,B)のマスに1を代入
	for (int i = 0; i < N; ++i) {
		++sum[A[i]][B[i]];
	}

    // for(int i=0;i<=R+1;i++){
    //     for(int j=0;j<=C+1;j++) cout<<sum[i][j]<<" ";
    //     cout<<endl;
    // }
    
    // 2次元累積和
	for (int i = 1; i <= R+1; ++i) {
		for (int j = 1; j <= C+1; ++j) {
			sum[i][j] += sum[i - 1][j];
		}
	}
	for (int i = 1; i <= R+1; ++i) {
		for (int j = 1; j <= C+1; ++j) {
			sum[i][j] += sum[i][j - 1];
		}
	}

    // 対応する範囲の人数を算出
	int answer = 0;
	for (int i = 1; i <= (R+1)-K; ++i) {
		for (int j = 1; j <= (C+1)-K; ++j) {
			answer = max(answer, sum[i-1][j-1] + sum[i+K][j+K] - sum[i-1][j+K] - sum[i+K][j-1]);
		}
	}

	cout << answer << endl;
	return 0;
}