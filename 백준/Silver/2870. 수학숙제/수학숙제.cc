#include <bits/stdc++.h>
using namespace std;
int n;
string input;

int myStoi(string s){
    int res = 0;
    for(char a : s){
        res = res*10+(a-'0');
    }
    return res;
}
int main() {
    cin >> n;
    vector<string> v;
    for(int i = 0; i<n; i++){
        cin >> input;
        string tmp;
        for(char a : input){
            if('0'<=a && a<='9'){
                tmp += a;
            } else {
                if(!tmp.empty()){
                    int start = 0;
                    while(start < tmp.size()-1 && tmp[start] == '0') start++;
                    v.push_back(tmp.substr(start));
                }
                tmp = "";
            }
        }
        if(tmp.size()) {
            int start = 0;
            while(start < tmp.size()-1 && tmp[start] == '0') start++;
            v.push_back(tmp.substr(start));
        }
    }
    sort(v.begin(), v.end(), [](const string& a, const string& b){
        if(a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    for(auto& i : v){
        cout << i << '\n';
    }
    return 0;
}