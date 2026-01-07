#include <bits/stdc++.h>
using namespace std;
int t, n;
int main() {
    cin >> t;

    while(t--) {
        cin >> n;
        map<string, int> clothes;
        
        for(int i = 0; i<n; i++){
            string type, name;
            cin >> name >> type;
            clothes[type]++;
        }  
        int result = 1;
        for(auto[type, cnt] : clothes){
            result *= (cnt+1);
        }
        result -= 1;
        cout << result << "\n";
    }

    return 0;
}