#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    cin >> a >> b;
    char tmp;
    cout << a.size() << " " << b.size() << '\n';
    cout << a + b << '\n';
    tmp = a[0];
    a[0] = b[0];
    b[0] = tmp;
    cout << a << ' ' << b << '\n';
    return 0;
}