#include <bits/stdc++.h>
using namespace std;
int n, c, a[1004];
vector<pair<int, int>> v;
map<int, int> mp, mp_first;//mp_first 는 숫자, 순서
bool cmp(pair<int, int> a, pair<int,int>b){
    if(a.first == b.first){
        return mp_first[a.second] < mp_first[b.second];
    }
    return a.first>b.first;
}
int main(){
    cin >> n >> c;
    int tmp;
    for(int i =0; i<n; i++){
        cin >> tmp; mp[tmp]++;
        if(mp_first[tmp] == 0) mp_first[tmp] = i+1;
    }
    for(auto it : mp){
        v.push_back({it.second, it.first});
        //갯수, 숫자
    }
    sort(v.begin(), v.end(), cmp);
    for(auto i : v){
        for(int j =0; j<i.first; j++){
            cout << i.second << ' ';
        }
    }
    
}