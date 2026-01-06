#include <bits/stdc++.h>
using namespace std;

int N, M;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;
    vector<string> numToName(N+1);
    map<string, int> nameToNum;

    for(int i = 1; i<=N; i++){
        string name;
        cin >> name;
        numToName[i] = name;
        nameToNum[name] = i;
    }

    for(int i = 0; i<M; i++){
        string input;
        cin >> input;

        if(input[0] >= '0' && input[0] <= '9') {
            cout << numToName[stoi(input)] << '\n';
        } 
        else {
            cout << nameToNum[input] << '\n';
        }
    }
    return 0;
}