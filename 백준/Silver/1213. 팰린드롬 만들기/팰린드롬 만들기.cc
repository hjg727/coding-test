#include <bits/stdc++.h>
using namespace std;
string sorry = "I'm Sorry Hansoo";
string input;
int cnt[200], flag;
int main() {
    int oddCnt = 0;

    cin >> input;
    for(char a : input) {
        cnt[a]++;
    }
    for(char a = 'A'; a <='Z'; a++){
        if(cnt[a]&1) oddCnt++;
    }

    if(oddCnt > 1) {
        cout << sorry << '\n';
        return 0;
    }
    char mid = '\0';
    string ret = "";
    for(char i = 'Z'; i>='A'; i--){
        if(cnt[i]){
            if(cnt[i]&1) {
                mid = char(i);
                cnt[i]--;
            }

            for(int j = 0; j<cnt[i]; j+= 2){
                ret = char(i) + ret;
                ret += char(i);
            }
        }
    }

    if(mid) ret.insert(ret.begin()+ret.size()/2, mid);
    cout << ret << '\n';
    return 0;
}