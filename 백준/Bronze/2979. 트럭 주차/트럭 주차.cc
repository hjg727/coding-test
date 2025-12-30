// 1대 1분에 한대당 A원, 2대 B원, 3대 C원
#include <bits/stdc++.h>
using namespace std;
int A, B, C;
int cnt[101];
int hap;
int main() {
    cin >> A >> B >> C;
    for(int i = 0; i<3; i++) {
        int x, y;
        cin >> x >> y;
        for(int j = x; j<y; j++) cnt[j]++;
    }

    for(int i=1; i<101; i++) {
        if(cnt[i]==0) continue;
        else if(cnt[i]==1) hap += A;
        else if(cnt[i]==2) hap += B*2;
        else hap += C*3;
    }
    cout << hap << "\n";
    return 0;
}