#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t){
        t-=1;

        ll num;
        cin >> num;
        ll cnt = 0;
        while(num>=5){
            num /=5;
            cnt += num;
        }
        cout << cnt << '\n';
    }
    return 0;
} 