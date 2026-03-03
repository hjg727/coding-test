#include <bits/stdc++.h>
using namespace std;
int n;
int main() {
    cin >> n;
    int cnt = 0;
    int num = 666;
    while(1){
        if(to_string(num).find("666") != string::npos){
            cnt += 1;
        }
        if (cnt == n){
            cout << num << "\n";
            break;
        }
        num += 1;
    }
    return 0;
}