#include <bits/stdc++.h>
using namespace std;
int N;
string pattern, prev, next;
string input;
int main() {
    cin >> N;
    cin >> pattern;
    
    int star = pattern.find('*');
    string prev = pattern.substr(0, star);
    string next = pattern.substr(star+1);

    for(int i = 0; i<N; i++){
        cin >> input;
        
        if(input.length() < prev.length()+next.length()) {
            cout <<"NE\n";
            continue;
        }
        
        if(input.substr(0, prev.length()) == prev && input.substr(input.length() - next.length()) == next) {
            cout << "DA\n";
            continue;
        }

        cout << "NE\n";
    }
    return 0;
}