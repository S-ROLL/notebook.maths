# Data structure and Algorithm
!!! info
    Source: <font size="1">[Programiz](https://www.programiz.com/dsa){ .md-button }</font>

## Sorting
### Bubble sort

Mã giả

```
bubbleSort(array)
  for i <- 1 to sizeOfArray - 1
    for j <- 1 to sizeOfArray - 1 - i
      if leftElement > rightElement
        swap leftElement and rightElement
end bubbleSort
```

!!! Code
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        void bubbleSort(int array[], int size) {
            for (int step = 0; step < size -1; ++step) {
                for (int i = 0; i < size - step - 1; ++i) {
                    if (array[i] > array[i + 1]) {
                        int temp = array[i];
                        array[i] = array[i + 1];
                        array[i + 1] = temp;
                    }
                }
            }
        }

        void printArray(int array[], int size) {
            for (int i = 0; i < size; ++i) {
                cout << "  " << array[i];
            }
            cout << "\n";
        }

        int main() {
            int data[] = {-2, 45, 0, 11, -9};
            int size = sizeof(data) / sizeof(data[0]);
            bubbleSort(data, size);
            cout << "Sorted Array in Ascending Order:\n";  
            printArray(data, size);
        }
        ```
    === "Python"
        ```py
        def bubbleSort(array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

        data = [-2, 45, 0, 11, -9]
        bubbleSort(data)
        print('Sorted Array in Ascending Order:')
        print(data)
        ```