#include <bits/stdc++.h>
using namespace std;

int m, n, k;
int grid[104][104];
int visited[104][104];
const int dy[] = {-1,1,0,0};
const int dx[] = {0,0,-1,1};
vector<int> res;
int cnt;
void dfs(int sy, int sx) {
    visited[sy][sx] = 1;
    for(int i = 0; i<4; i++){
        int ny = sy+dy[i];
        int nx = sx+dx[i];

        if(0<=ny && ny<m && 0<=nx && nx<n && grid[ny][nx] != 2 && !visited[ny][nx]){
            dfs(ny,nx);
            cnt += 1;
        }
    }
    return;
}
int main(){
    cin >> m >> n >> k;
    for(int i = 0; i<k; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for(int i =y1; i<y2; i++){
            for(int j = x1; j<x2; j++){
                grid[i][j] = 2;
            }
        }
    }
    
    for(int i =0; i<m; i++){
        for(int j= 0; j<n; j++){
            if(grid[i][j]!=2 && !visited[i][j]){
                cnt = 1;
                dfs(i,j);
                res.push_back(cnt);
            }
        }
    }
    sort(res.begin(),res.end());
    cout<<res.size() << '\n';
    for(int a : res){
        cout << a << ' ';
    }
    return 0;
}