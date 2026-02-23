#include <bits/stdc++.h>
using namespace std;
int n;
string grid[64];

void solve(int y, int x, int size){
    bool check = true;
    for(int i = y; i<y+size; i++){
        for(int j = x; j<x+size; j++){
            if(grid[y][x] != grid[i][j]){
                check = false;
                break;
            }
        }
    }
    if(check) {
        cout << grid[y][x];
    } else {
        cout << '(';
        int half = size/2;
        solve(y, x, half);
        solve(y, x+half, half);
        solve(y+half, x, half);
        solve(y+half, x+half, half);
        cout<< ')';
    }
}

int main(){
    cin >> n;
    for(int i = 0; i<n; i++){
        cin >> grid[i];
    }
    solve(0, 0, n);
}