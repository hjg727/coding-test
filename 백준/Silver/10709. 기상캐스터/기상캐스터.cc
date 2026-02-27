#include <bits/stdc++.h>
using namespace std;
//1분마다 -> 1키로미터씩
// 각 구역마다 지금부터몇분뒤에 구름이 오는지!
// 구름있으면 c 없으면 .

//처음부터 구름이있으면 0 몇분이 지나도 뜨지않을경우 -1 나머진 몇분이후 뜰지 정수로 표현
int h, w;

vector<int> cloud(string& a){
    vector<int> v;
    int tmp = -1;
    for(auto& c : a){
        if(c== 'c') {tmp = 0; v.push_back(tmp);}
        else{
            if(tmp <0) {
                v.push_back(tmp);
            } else {
                tmp+=1;
                v.push_back(tmp);
            }
        }
    }
    return v;
}
int main(){
    cin >> h >> w;
    vector<vector<int>> v;
    for(int i =0; i<h; i++){
        string tmp;
        cin >> tmp;

        v.push_back(cloud(tmp));
    }

    for(auto& row : v){
        for(auto& col : row){
            cout << col << ' ';
        }
        cout << '\n';
    }
    return 0;
}