#include <bits/stdc++.h>
using namespace std;
//인덱스와 숫자의 크기를 헷갈리지말자
int n, a[1000004], ret[1000004];
stack<int> s;
int main() {
    cin >> n;
    memset(ret, -1, sizeof(ret));
    for(int i =0; i<n; i++){
        cin >> a[i];
        while(s.size() && a[s.top()] < a[i]){
            ret[s.top()] = a[i];
            s.pop();
        }
        s.push(i);
    }

    for(int i = 0; i < n; i++) cout << ret[i] << ' ';
    return 0;
    
}