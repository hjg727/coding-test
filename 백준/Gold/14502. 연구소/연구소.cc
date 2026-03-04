#include <bits/stdc++.h>
using namespace std;
int grid[8][8];
int tmp[8][8];
int n, m, res;
const int wall = 3;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
void bfs(){
    queue<pair<int,int>> q;
    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            if(tmp[i][j] == 2){
                q.push({i,j});
            }
        }
    }

    while(q.size()){
        int cy, cx;
        tie(cy,cx) = q.front();
        tmp[cy][cx] = 2;
        q.pop();
        for(int i = 0; i<4; i++){
            int ny = cy+dy[i];
            int nx = cx+dx[i];

            if(0<=ny && ny<n && 0<=nx && nx<m && tmp[ny][nx] == 0){
                q.push({ny, nx});
            }
        }
    }
    int safeArea = 0;
    for(int i=0; i<n; i++){
        for(int j = 0; j<m; j++){
            if(tmp[i][j] == 0) safeArea++;
        }
    }
    res = max(res, safeArea);
}
void makeWall(int cnt) {
    if(cnt==wall){
        memcpy(tmp, grid, sizeof(grid));
        bfs();
        return;
    }
    for(int i =0; i<n; i++){
        for(int j =0; j<m; j++){
            if(grid[i][j]==0){
                grid[i][j] = 1;
                makeWall(cnt+1);
                grid[i][j] = 0;
            }
        }
    }
}
int main() {
    cin >> n >> m;
    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            cin >> grid[i][j];
        }
    }
    makeWall(0);

    cout << res;
    return 0;
}