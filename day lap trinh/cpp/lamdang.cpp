#include <iostream>
using namespace std;

void nhap(int a[], int &n) {
    cout<<"Nhap vao n: "; cin>>n;
    for (int i=0; i<n; i++) {
        cout<<"Nhap vao so thu "<<i+1<<": ";
        cin>>a[i];
    }
}

void sapxep(int a[], int &n) {
    for (int i=0; i<n-1; i++) {
        for (int j=i+1; j<n; j++) {
            if (a[i]>a[j])
                swap(a[i],a[j]);
        }
    }
    cout<<"Sap duoc sap xep: ";
    for (int i=0; i<n; i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

int main () {
    int a[1000], n;
    nhap(a,n);
    sapxep(a,n);
}