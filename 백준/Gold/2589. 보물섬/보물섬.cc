#include <bits/stdc++.h>
using namespace std;
int n, m, mx;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
//육지 L 바다 W
int grid[54][54];
int visited[54][54];

int bfs(int y, int x){
    int dist[54][54];
    memset(dist, -1, sizeof(dist));
    int cnt = 0;
    queue<pair<int,int>> q;
    q.push({y, x});
    dist[y][x] = 0;
    while(q.size()){
        int cx, cy;
        tie(cy, cx) = q.front();
        q.pop();

        for(int i = 0; i<4; i++){
            int ny = cy+dy[i];
            int nx = cx+dx[i];

            if(0<=ny && ny<n && 0<=nx && nx<m && grid[ny][nx] > 0 && dist[ny][nx] == -1){
                dist[ny][nx] = dist[cy][cx]+1;
                cnt = max(cnt, dist[ny][nx]);
                q.push({ny, nx});
            }
        }
    }
    return cnt;
}

int main() {
    cin >> n >> m;

    for(int i = 0; i< n; i++){
        for(int j = 0; j<m; j++){
            char tmp;
            cin >> tmp;
            grid[i][j] = (tmp == 'L')? 1 : 0;
        }
    }
    for(int i =0; i<n; i++){
        for(int j = 0; j<m; j++){
            if(grid[i][j]) {
                mx = max(mx, bfs(i, j));
            }
        }
    }
    cout << mx <<'\n';
    return 0;

}