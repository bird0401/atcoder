#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int W, N;
	cin >> W >> N;
	vector<int> L(N), R(N);
	vector<int> compression;
    for (int i = 0; i < N; ++i) {
		cin >> L[i] >> R[i];
		--L[i];
        compression.push_back(L[i]);
		compression.push_back(R[i]);
	}

	sort(compression.begin(), compression.end());
	compression.erase(unique(compression.begin(), compression.end()), compression.end()); //leave unique value

    // for (auto& e:compression) cout<<e<<" ";
    // cout<<endl;

	for (int i = 0; i < N; ++i) {
		L[i] = lower_bound(compression.begin(), compression.end(), L[i]) - compression.begin();
		R[i] = lower_bound(compression.begin(), compression.end(), R[i]) - compression.begin();
        // cout<<L[i]<<" "<<R[i]<<endl;
	}
	vector<int> h(compression.size() - 1);
	for (int i = 0; i < N; ++i) {
		int height = *max_element(h.begin() + L[i], h.begin() + R[i]) + 1;
		fill(h.begin() + L[i], h.begin() + R[i], height);
		cout << height << '\n';
	}
    // for (auto& e:h) cout<<e<<" ";
    // cout<<endl;
	return 0;
}