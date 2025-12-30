#include <bits/stdc++.h>
using namespace std;
string result;
int N;
int cnt[26];
int main() {
    string surrender = "PREDAJA";
    
    cin >> N;

    for(int i = 0; i<N; i++){
        string tmp;
        cin >> tmp;
        cnt[tmp[0] - 'a']++;
    }
    for(int i =0; i<26; i++){
        if(cnt[i]>=5) result += char(i+'a');
    }
    if(!result.empty()) cout << result << '\n';
    else cout << surrender << '\n';
}