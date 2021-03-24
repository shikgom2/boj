#include <stdio.h>
#include <iostream>
using namespace std;

unsigned long long f(unsigned long long  a, unsigned long long  b, unsigned long long  c)
{
    if (b == 0)
        return 1;
    if (b == 1)
        return a % c;

    unsigned long long temp = f(a, b / 2, c);

    if (b & 1)
        return temp * temp % c * a % c;
    else
        return temp * temp % c;
}

int main(){
	int a,b,c;
	
	cin >> a >> b >> c;
	int k = f(a,b,c);	
	cout << k << endl;
}
