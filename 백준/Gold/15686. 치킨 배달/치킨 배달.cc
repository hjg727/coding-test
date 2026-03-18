#include <bits/stdc++.h>
using namespace std;
int n, m;
int res = INT_MAX;
int grid[54][54];
vector<pair<int,int>> c;
vector<pair<int, int>> h;
int dist(pair<int, int> c, pair<int, int> h){
    return abs(c.first-h.first) + abs(c.second-h.second);
}
int cal(vector<int>& picked){
    int tmp = 0;
    for(auto& a : h){
        int min_dist = INT_MAX;
        for(int i : picked){
            int d = dist(a, c[i]);
            min_dist = min(d, min_dist);
        }
        tmp += min_dist;
    }
    return tmp;
}
void recur(int start, vector<int>& picked){
    if(picked.size() == m){
        res = min(res, cal(picked));
        return;
    }
    for(int i = start; i<c.size(); i++){
        picked.push_back(i);
        recur(i+1, picked);
        picked.pop_back();
    }
}
int main() {
    cin >> n >> m;

    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            cin >> grid[i][j];
            if(grid[i][j] == 2){
                c.push_back({i, j});
            }else if(grid[i][j] == 1){
                h.push_back({i, j});
            }
        }
    }
    vector<int> v;
    recur(0, v);
    cout << res;
    return 0;

}