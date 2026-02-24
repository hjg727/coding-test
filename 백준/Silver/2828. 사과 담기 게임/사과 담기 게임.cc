#include <bits/stdc++.h>

using namespace std;

int n, m, j, res;
int main() {
    cin >> n >> m;
    int start = 1;
    cin >> j;
    while(j){
        int apple;
        cin >> apple;

        if(apple < start){
            res += start-apple;
            start = apple;
        } else if(apple > start+m-1){
            res += (apple - (start+m-1));
            start = apple-m+1;
        }
        j-=1;
    }

    cout << res;
    return 0;
}