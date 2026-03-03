#include <bits/stdc++.h>
using namespace std;

string a;
int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    while(getline(cin, a)){
        if(a== ".") break;

        stack<char> st;
        bool flag = true;
        for(char& c : a){
            if(c == '(' || c == '['){
                st.push(c);
            } else if (c == ')'){
                if(st.empty() || st.top() != '('){
                    flag = false;
                    break;
                }
                st.pop();
            } else if (c == ']'){
                if(st.empty() || st.top() != '['){
                    flag = false;
                    break;
                }
                st.pop();
            }
        }

        if(!flag || st.size()){
            cout << "no" << '\n';
        } else {
            cout << "yes" << '\n';
        }
    }

    return 0;
}