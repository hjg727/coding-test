#include <bits/stdc++.h>
using namespace std;
int n;
int main() {

    while(cin >> n) {

        int cnt = 1;
        long long num = 1;

        while(num%n != 0){
            num = (num * 10 + 1) % n;
            cnt++;
        }

        cout << cnt << "\n";
    }

    return 0;
}