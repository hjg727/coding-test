#include <bits/stdc++.h>
using namespace std;

int main() {
    map<int, int> cnt;
    int res = 0;
    int n = 0;
    int m = 0;
    cin >> n;
    cin >> m;

    vector<int> v(n);
    for(int &x : v) cin >> x;

    for(int x : v){
        if(cnt[m-x]) res+=1;
        cnt[x]++;
    }
    cout << res;
    return 0;
}