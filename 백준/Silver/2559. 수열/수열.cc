#include <bits/stdc++.h>
using namespace std;

int main(){
    
    int N, K;
    cin >> N >> K;
    
    vector<int> input(N);
    
    for(int i = 0; i<N; i++){
        cin >> input[i];
    }

    int sum = 0;
    for(int i = 0; i<K; i++){
        sum += input[i];
    }
    int res = sum;

    for(int i = K; i<N; i++){
        sum += input[i];
        sum -= input[i-K];
        res = max(res, sum);
    }
    
    cout << res;
    return 0;
}