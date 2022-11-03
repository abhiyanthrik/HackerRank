#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    int tmp;
    char ch;
    vector <int> vec;
    stringstream s(str);
    while(s>>tmp){
        vec.push_back(tmp);
        s>>ch;
    }
    return vec;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}