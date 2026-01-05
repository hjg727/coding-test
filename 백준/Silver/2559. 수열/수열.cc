#include <bits/stdc++.h>
using namespace std;
int N, K, res;
//res가 0여서 -값이 최댓값보다 0이 나옴
vector<int> input;
int main(){
    cin >> N >> K;

    for(int i = 0; i<N; i++){
        int x;
        cin >> x;
        input.push_back(x);
    }
    for(int i = 0; i<K; i++){
        res += input[i];
    }

    for(int i = 1; i<=N-K; i++){
        int tmp = 0;
        for(int j = i; j<i+K; j++){
            tmp += input[j];
        }
        res = max(tmp, res);
    }
    cout << res;
    return 0;
}