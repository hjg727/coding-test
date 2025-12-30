#include <bits/stdc++.h>
using namespace std;
string input, result;
int main() {
    getline(cin, input);

    for(char a : input) {
        if(a>='a'&& a<='z') {
            a = ((a-'a'+13)%26) + 'a';
        }
        else if(a>='A'&& a<='Z'){
            a = ((a-'A'+13)%26) + 'A';
        } 
        result += a;
    }
    cout << result <<'\n';
    return 0;
}