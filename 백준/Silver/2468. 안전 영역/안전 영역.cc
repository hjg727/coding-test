#include <bits/stdc++.h>
using namespace std;
int n;
int field[104][104];
int visited[104][104];
const int dy[] = {0,0,-1,1};
const int dx[] = {-1,1,0,0};
void bfs(int y, int x, int h){
    visited[y][x] = 1;
    queue<pair<int,int>> q;
    q.push({y,x});

    while(q.size()){
        int cy, cx;
        tie(cy,cx) = q.front();
        q.pop();

        for(int i = 0; i<4; i++){
            int ny = cy+dy[i];
            int nx = cx+dx[i];

            if(0<=ny&&ny<n&&0<=nx&&nx<n&&field[ny][nx]>h&&!visited[ny][nx]){
                visited[ny][nx] = 1;
                q.push({ny,nx});
            }
        }
    }
    return;
}
int main() {
    cin >> n;
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            cin >> field[i][j];
        }
    }
    int res = -1;
    for(int h = 0; h<=100; h++){
        int tmp = 0;
        memset(visited, 0, sizeof(visited));
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(field[i][j] > h && !visited[i][j]){
                    bfs(i,j,h);
                    tmp++;
                }
            }
        }
        res = max(res, tmp);
    }

    cout<<res;
    return 0;
}