#include <bits/stdc++.h>
using namespace std;
string input, sub;
int length;
int main() {
    cin >> input;

    length = input.size();
    sub = input;
    reverse(sub.begin(), sub.end());
    if(sub == input) cout << 1 << '\n';
    else cout << 0 << '\n';
    return 0;
}