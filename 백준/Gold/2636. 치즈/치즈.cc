#include <bits/stdc++.h>
using namespace std;
int grid[104][104];
int n, m, a, cheese, res;

int dy[] = {0,0,-1,1};
int dx[] = {-1,1,0,0};


void bfs(vector<pair<int,int>>& ch_pos){
    queue<pair<int,int>> q;
    
    int visited[104][104] = {};
    int ch_visited[104][104] = {};
    q.push({0,0});

    while(q.size()){
        int cy,cx;
        tie(cy,cx) = q.front();
        q.pop();
        for(int i = 0; i<4; i++){
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if(ny<0 || n<=ny || nx<0 || m<=nx) continue;
            if(grid[ny][nx] == 1 && !ch_visited[ny][nx]){
                ch_visited[ny][nx] = 1;
                ch_pos.push_back({ny,nx});
            } else if(grid[ny][nx] == 0 && !visited[ny][nx]){
                visited[ny][nx] = 1;
                q.push({ny,nx});
            }
        }
    }
}

int main() {
    cin >> n >> m;

    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            cin >> grid[i][j];
            if(grid[i][j]==1) cheese+= 1;
        }
    }
    
    while(cheese > 0){
        vector<pair<int,int>> ch_pos;
        bfs(ch_pos);
        a++;
        res = ch_pos.size();

        for(auto[y,x] : ch_pos) grid[y][x] = 0;
        cheese -= res;
    }

    cout << a <<'\n';
    cout << res <<'\n';
    return 0;

}