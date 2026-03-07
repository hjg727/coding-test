//신뢰하는 관계와 신뢰하지않는 관계
//신뢰 -> a가b를 신뢰하면 b->a ㄱㄴ 
#include <bits/stdc++.h>
using namespace std;

int n, m;
int mx;
vector<int> adj[10001];

int dfs(int node,vector<bool>& visited){
    visited[node] = true;
    int cnt = 1;
    for(int child : adj[node]){
        if(!visited[child]) cnt += dfs(child, visited);
    }
    return cnt;
}
int main() {
    cin >> n >> m;
    vector<int> cnt;
    for(int i =0; i<m; i++){
        int a, b;
        cin >> a >> b;
        adj[b].push_back(a);
    }

    for(int i = 1; i<=n; i++){
        vector<bool> visited(n+1, false);
        cnt.push_back(dfs(i, visited));
    }
    mx = *max_element(cnt.begin(), cnt.end());

    for(int i = 1; i<=n; i++){
        if(cnt[i-1] == mx) cout << i << ' ';
    }
    return 0;
}