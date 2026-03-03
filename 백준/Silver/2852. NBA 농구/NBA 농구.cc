#include <bits/stdc++.h>
using namespace std;
int n;
int pre_time;
int one, two;
string int_to_string(int num){
    int a = num/60;
    int b = num%60;
    string mm = (a < 10 ? "0" : "") + to_string(a);
    string ss = (b < 10 ? "0" : "") + to_string(b);
    return mm + ":" + ss;
}

int string_to_int(string num){
    int idx = num.find(":");
    int mm = stoi(num.substr(0, idx));
    int ss = stoi(num.substr(idx+1));
    return mm*60+ss;
}
int main() {
    cin >> n;
    int a = 0; int b = 0;
    for(int i = 0; i<n; i++){
        string team, tmp;
        cin >> team >> tmp;
        int time = string_to_int(tmp);
        if(one > two ){
            a += (time - pre_time);
        }else if(two > one) {
            b += (time - pre_time);
        }

        team == "1" ? one++ : two++;
        pre_time = time;
    }
    if(one > two ){
        a += (string_to_int("48:00") - pre_time);
    }else if(two > one) {
        b += (string_to_int("48:00") - pre_time);
    }
    

    cout << int_to_string(a) << '\n';
    cout << int_to_string(b) << '\n';
    
    
    return 0;
}