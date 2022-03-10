#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main(){
    int t;
    cin>>t;
    vector<pair<int,int>> m(t);
    rep(i,t){
        cin>>m.at(i).first>>m.at(i).second;
    }
    vector<int64_t> nums(t);
    rep(i,t){
        int64_t min_c=m.at(i).first;
        int64_t max_c=m.at(i).second;
        if (max_c-min_c>=min_c){
            int64_t sum=(1+(max_c-2*min_c+1))*(max_c-2*min_c+1)/2;
            nums.at(i)=sum;
        }else nums.at(i)=0;
    }
    rep(i,t) cout<<nums[i]<<endl;

}

