#include <bits/stdc++.h>

using namespace std;

int dwarf[9];
int sum = 0;

int main() {
    for(int i = 0; i<9; i++) {
        cin >> dwarf[i];
        sum += dwarf[i];
    }
    
    int diff = 0;
    diff = sum - 100;
    sort(dwarf, dwarf+9);
    for(int i = 0; i<9; i++){
        for(int j = i+1; j<9; j++){
            if(dwarf[i]+dwarf[j] == diff){
                for(int k = 0; k<9; k++) {
                    if(k!=i && k!=j){
                        cout << dwarf[k] << '\n';                    
                    }
                }
                return 0;
            }
        }
    }

    return 0;
}