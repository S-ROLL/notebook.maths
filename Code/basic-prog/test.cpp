#include <iostream>
#include <math.h>

using namespace std;

long t

int main()
{
    cout << "nhap do";
    cin >> t;

    cout << "gio" << t / 3600 ;
    cout << "phut" << (t%3600)/60;
    cout << "giay" << t%60;
    

    return 0;
}