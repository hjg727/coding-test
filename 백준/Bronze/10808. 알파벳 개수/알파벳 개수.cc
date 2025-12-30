#include <bits/stdc++.h>
using namespace std;
int cnt[26] = {0};
string input;
int main() {
    cin >> input;
    for(char a : input){
        cnt[a-'a']++;
    }

    for(int i=0; i<26; i++){
        cout << cnt[i] << " ";
    }
    return 0;
}