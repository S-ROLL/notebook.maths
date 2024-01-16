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