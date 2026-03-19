#include <bits/stdc++.h>
using namespace std;

int r,c;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
int visited[1004][1004];
char grid[1004][1004];
int fire[1004][1004];

int main() {
    cin >> r >> c;
    queue<pair<int,int>> ji;
    queue<pair<int,int>> f;
    for(int i = 0; i<r; i++){
        for(int j = 0; j<c; j++){
            cin >> grid[i][j];
            if(grid[i][j]=='F') f.push({i,j});
            else if(grid[i][j] == 'J') ji.push({i,j});
        }
    }
    int day = 0;
    visited[ji.front().first][ji.front().second] = 1;
    fire[f.front().first][f.front().second] = 1;
    while(true) {
        int f_size = f.size();
        for(int i = 0; i<f_size; i++){
            int y = f.front().first;
            int x = f.front().second;
            f.pop();

            for(int d = 0; d<4; d++){
                int ny = y + dy[d];
                int nx = x + dx[d];
                if(ny<0 || ny>=r || nx<0 || nx>=c) continue;
                if(grid[ny][nx] == '#') continue;
                if(fire[ny][nx]) continue;
                fire[ny][nx] = 1;
                f.push({ny,nx});
            }
        }
        int ji_size = ji.size();
        for(int i = 0; i<ji_size; i++){
            int y = ji.front().first;
            int x = ji.front().second;
            ji.pop();

            for(int d = 0; d<4; d++){
                int ny = y + dy[d];
                int nx = x + dx[d];

                if(ny<0 || ny>=r || nx<0 || nx>=c){
                    cout << day+1;
                    return 0;
                }
                if(fire[ny][nx]) continue;
                if(grid[ny][nx] == '#') continue;
                if(visited[ny][nx]) continue;
                
                visited[ny][nx] = 1;
                ji.push({ny,nx});
            }
        }
        

        if(ji.empty()){
            cout << "IMPOSSIBLE";
            return 0;
        }
        day++;
    }

}