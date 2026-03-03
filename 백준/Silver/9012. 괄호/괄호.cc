#include <bits/stdc++.h>
using namespace std;
int n;

int main() {
    cin >> n;
    while(n){
        stack<char> st;
        string a;
        bool flag = true;
        cin >> a;
        for(char& c : a) {
            if(c == '('){
                st.push(c);
            } else {
                if(st.empty()) { flag = false; break; }
                st.pop();
            }
        }
        if(!flag || st.size()){
            cout << "NO" << '\n';
        } else {
            cout << "YES" << '\n';
        }

        n-=1;
    }

    return 0;
}