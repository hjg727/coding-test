#include <bits/stdc++.h>
using namespace std;
int n, l, r;
int grid[54][54];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
int main() {
    cin >> n >> l >> r;

    for(int i = 0; i<n; i++)
        for(int j =0; j<n; j++)
            cin >> grid[i][j];
        
    
    int day = 0;

    while(true) {
        bool moved = false;
        bool visited[54][54] = {};

        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(visited[i][j]) continue;

                queue<pair<int,int>> q;
                vector<pair<int,int>> v;

                q.push({i,j});
                visited[i][j] = true;
                v.push_back({i,j});

                while(q.size()){
                    int y = q.front().first;
                    int x = q.front().second;
                    q.pop();

                    for(int z=0; z<4; z++){
                        int nx = x + dx[z];
                        int ny = y + dy[z];

                        if(nx<0 || nx >=n || ny < 0 || ny >= n) continue;
                        if(visited[ny][nx]) continue;

                        int diff = abs(grid[y][x] - grid[ny][nx]);
                        if(diff<l || diff >r) continue;
                        
                        visited[ny][nx] = true;
                        q.push({ny,nx});
                        v.push_back({ny,nx});
                    }
                }

                if(v.size() >=2){
                    moved = true;
                    int total = 0;
                    for(int k = 0; k < v.size(); k++) total += grid[v[k].first][v[k].second];
                    int avg = total / v.size();
                    for(int k = 0; k < v.size(); k++) grid[v[k].first][v[k].second] = avg;
                }
            }
        }

        if(!moved) break;
        day++;
    }
    cout << day << endl;
    return 0;
}