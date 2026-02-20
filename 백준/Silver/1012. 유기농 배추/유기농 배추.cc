#include <bits/stdc++.h>
using namespace std;
int n, m, t, k;
int field[51][51];
int visited[51][51];

const int dy[] = {0,0,-1,1};
const int dx[] = {-1,1,0,0};

void dfs(int y, int x){
    visited[y][x]= 1;
    for(int i = 0; i<4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];

        if(0<=ny && ny<n && 0<=nx && nx<m && field[ny][nx] && !visited[ny][nx]){
            dfs(ny, nx);
        }
    }
}

int main() {
    cin >> t;

    while(t){
        t -= 1;
        cin >> n >> m >> k;
        int ans = 0;
        for(int i = 0; i<k; i++){
            int y,x;
            cin >> y >> x;
            field[y][x] = 1;
        }

        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                if(field[i][j] && !visited[i][j]){
                    dfs(i,j);
                    ans++;
                }
            }
        }
        memset(field, 0, sizeof(field));
        memset(visited, 0, sizeof(visited));
        cout << ans << '\n';

    }
    return 0;
}