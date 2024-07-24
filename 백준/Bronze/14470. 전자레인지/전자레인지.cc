
#include <iostream>
using namespace std;
int main()
{
    int a,b,c,d,e;
    
    cin >> a >> b >> c >> d >> e;
    int toMelt = d;
    int toB = e * b;
    if (a < 0) {
        int toZero = -1 * a * c;
        cout<< toZero + toMelt + toB << "\n";
    }
    else if ( a > 0 ) {
        int toB = e * (b-a);
        cout << toB << "\n";
    } 
    else {
        cout << toMelt + toB <<'\n';
    }

    return 0;
}