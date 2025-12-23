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
    set<int> bad_dwarf;
    bool found = false;
    for(int i = 0; i < 9; i++){
        if(found) break;
        for(int j = i+1; j<9; j++) {
            if (dwarf[i] + dwarf[j] == diff) {
                bad_dwarf.insert(i);
                bad_dwarf.insert(j);
                found = true;
                break;
            }
        }
    }  
    vector<int> result;
    for(int i = 0; i<9; i++){
        if(bad_dwarf.count(i)){
            continue;
        } else {
            result.push_back(dwarf[i]);
        }
    }
    sort(result.begin(), result.end());
    for(int a : result) cout << a << "\n";
    return 0;
    
}