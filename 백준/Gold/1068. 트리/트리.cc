#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> adj[100];
int dfs(int node, int tg){
    if(node == tg) return 0;

    int cnt = 0;
    for(int child : adj[node]){
        if(child != tg) cnt += dfs(child, tg);
    }
    if(cnt == 0) return 1;
    return cnt;
}
int main() {
    cin >> n;
    int root = 0;
    for(int i =0; i<n; i++){
        int tmp;
        cin >> tmp;
        if(tmp == -1) root = i;
        else adj[tmp].push_back(i);
    }
    int tg;
    cin >> tg;
    if(root == tg) {
        cout << 0 << '\n';
        return 0;
    }
    int cnt = dfs(root, tg);
    cout << cnt << '\n';
    return 0;
}