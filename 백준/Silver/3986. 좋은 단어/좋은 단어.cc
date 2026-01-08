#include <bits/stdc++.h>
using namespace std;
stack<char> stk;
int n, res;
string input;
int main() {
    cin >> n;

    for(int i = 0; i<n; i++){
        cin>>input;
        
        for(char a : input){
            if(stk.empty()){
                stk.push(a);
            }
            else{
                if(stk.top() == a) stk.pop();
                else stk.push(a);
            }
        }
        if(stk.empty()) res++;
        else stk = stack<char>();
    }
    cout << res;
    return 0;
}