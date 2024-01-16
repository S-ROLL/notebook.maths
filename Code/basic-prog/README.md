#CPP
```cpp
#include<iostream.h>
#include<math.h>
int main()
{
    int a; // bien a thuoc kieu so nguyen
    cout<<"Moi ban nhap vao so a: ";
    cin>>a;
    int i=-4;
    int j=-i;
    double k = i * sqrt(2);
    cout<<"Gia tri i la: "<<i<<endl;
    cout<<"Gia tri j la: "<<j<<endl;
    cout<<"Gia tri k la: "<<k<<endl;
    return 0;
}
```
$f(x)=\frac{1}{x}$ with $x$ ranging from $0$ to $1$ in steps of $0.1$
```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    // Set precision for decimal points
    cout << fixed << setprecision(2);

    // Display the header of the table
    cout << "  x  | f(x) = 1/sqrt(x) " << endl;
    cout << "-----------------------" << endl;

    // Loop from 1 to 10
    for (int x = 1; x <= 10; x++) {
        // Calculate 1/sqrt(x)
        double fx = 1 / sqrt(x);

        // Display the current values of x and f(x)
        cout << "  " << x << "  | " << fx << endl;
    }

    return 0;
}
```
$f(x)=2x$ with $x$ ranging from $0$ to $10$ in steps of $1$
```cpp
#include <iostream>
using namespace std;

int main() {
    // Display the header of the table
    cout << " x | 2x " << endl;
    cout << "-----------" << endl;

    // Loop from 1 to 10
    for (int x = 1; x <= 10; x++) {
        // Calculate 2x
        int y = 2 * x;

        // Display the current values of x and 2x
        cout << " " << x << " | " << y << endl;
    }

    return 0;
}
```