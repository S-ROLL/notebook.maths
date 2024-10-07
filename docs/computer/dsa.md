# Data structure and Algorithm
!!! info
    Source: <font size="1">[Programiz](https://www.programiz.com/dsa){ .md-button }</font>

## Sorting
### Bubble sort

Ý tưởng của Bubble Sort là lặp lại việc so sánh cặp phần tử liền kề và hoán đổi chúng nếu chúng đang ở sai thứ tự, quá trình này được lặp lại cho đến khi mảng được sắp xếp hoàn toàn.

```py
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

### Selection sort

Ý tưởng của Selection Sort là lặp lại việc tìm phần tử nhỏ nhất trong phần chưa được sắp xếp của mảng và hoán đổi nó với phần tử đầu tiên của phần đó cho đến khi mảng được sắp xếp hoàn toàn.

```py
selectionSort(array, size)
  for i from 0 to size - 1 do
    set i as the index of the current minimum
    for j from i + 1 to size - 1 do
      if array[j] < array[current minimum]
        set j as the new current minimum index
    if current minimum is not i
      swap array[i] with array[current minimum]
end selectionSort
```

!!! Code
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        void swap(int *a, int *b) {
            int temp = *a;
            *a = *b;
            *b = temp;
        }

        void printArray(int array[], int size) {
            for (int i = 0; i < size; i++) {
                cout << array[i] << " ";
            }
            cout << endl;
        }

        void selectionSort(int array[], int size) {
            for (int i = 0; i < size - 1; i++) {
                int min_idx = i;
                for (int j = i + 1; j < size; j++) {
                    if (array[j] < array[min_idx])
                        min_idx = j;
                    }
                    swap(&array[min_idx], &array[i]);
            }
        }

        int main() {
            int data[] = {20, 12, 10, 15, 2};
            int size = sizeof(data) / sizeof(data[0]);
            selectionSort(data, size);
            cout << "Sorted array in Acsending Order:\n";
            printArray(data, size);
        }
        ```
    === "Python"
        ```py
        def selectionSort(array, size):
            for step in range(size):
                min_idx = step
                for i in range(step + 1, size):
                    if array[i] < array[min_idx]:
                        min_idx = i
                (array[step], array[min_idx]) = (array[min_idx], array[step])
        data = [-2, 45, 0, 11, -9]
        size = len(data)
        selectionSort(data, size)
        print('Sorted Array in Ascending Order:')
        print(data)
        ```

### Insertion sort

Ý tưởng của Insertion Sort là lặp lại việc lấy từng phần tử từ mảng chưa được sắp xếp, chèn nó vào vị trí đúng trong phần mảng đã được sắp xếp, tương tự như cách sắp xếp bài khi chơi bài tây.

```py
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
```

!!! Code
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        void printArray(int array[], int size) {
            for (int i = 0; i < size; i++) {
                cout << array[i] << " ";
            }
            cout << endl;
        }

        void insertionSort(int array[], int size) {
            for (int i = 1; i < size; i++) {
                int key = array[i];
                int j = i - 1;
                while (j >=0 && key < array[j]) {
                    array[j + 1] = array[j];
                    --j;
                }
                array[j + 1] = key;
            }
        }

        int main() {
            int data[] = {9, 5, 1, 4, 3};
            int size = sizeof(data) / sizeof(data[0]);
            insertionSort(data, size);
            cout << "Sorted array in ascending order:\n";
            printArray(data, size);
        }
        ```
    === "Python"
        ```py
        def insertionSort(array):
            for step in range(1, len(array)):
                key = array[step]
                j = step - 1
                while j >= 0 and key < array[j]:
                    array[j + 1] = array[j]
                    j = j - 1
                array[j + 1] = key
        data = [9, 5, 1, 4, 3]
        insertionSort(data)
        print('Sorted Array in Ascending Order:')
        print(data)
        ```


## Searching