#include <bits/stdc++.h>
using namespace std;
string ok = "is acceptable.";
string no = "is not acceptable.";
string input;


bool check(string a){
    string vowels = "aeiou";
    bool hasVowel = false;

    for(int i=0; i<a.size(); i++){
        if(vowels.find(a[i]) != string::npos) hasVowel = true;

        if(i>=1) {
            if(a[i] == a[i-1] && a[i] != 'e' && a[i] != 'o') return false;
        }

        if(i >= 2){
            bool cur = vowels.find(a[i]) != string::npos;
            bool p1 = vowels.find(a[i-1]) != string::npos;
            bool p2 = vowels.find(a[i-2]) != string::npos;
            if(cur == p1 && p1 == p2) return false;
        }
    }
    return hasVowel;
}

int main() {
    while(1){
        cin >> input;
        if(input == "end") break;
        if(check(input)){
            cout << '<' << input << "> " << ok << '\n';
        } else {
            cout << '<' << input << "> " << no << '\n';
        }
    }
}