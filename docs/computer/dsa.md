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
                    swap(array[min_idx], array[i]);
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

### Quick sort
Quick sort là một thuật toán sắp xếp chia để trị, hoạt động bằng cách chọn một phần tử gọi là phần tử trụ (pivot) và phân chia danh sách thành hai phần: một phần chứa các phần tử nhỏ hơn hoặc bằng phần tử trụ và một phần chứa các phần tử lớn hơn phần tử trụ, sau đó sắp xếp đệ quy hai phần này.

```py
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
```

!!! Code
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        void printArray(int array[], int size) {
            int i;
            for (i = 0; i < size; i++)
                cout << array[i] << " ";
            cout << endl;
        }

        int partition(int array[], int low, int high) {
            int pivot = array[high];
            int i = (low - 1);
            for (int j = low; j < high; j++) {
                if (array[j] <= pivot) {
                    i++;
                    swap(array[i], array[j]);
                }
            }
            swap(array[i + 1], array[high]);
            return (i + 1);
        }

        void quickSort(int array[], int low, int high) {
            if (low < high) {
                int pi = partition(array, low, high);
                quickSort(array, low, pi - 1);
                quickSort(array, pi + 1, high);
            }
        }

        int main() {
            int data[] = {8, 7, 6, 1, 0, 9, 2};
            int n = sizeof(data) / sizeof(data[0]);
            cout << "Unsorted Array: \n";
            printArray(data, n);
            quickSort(data, 0, n - 1);
            cout << "Sorted array in ascending order: \n";
            printArray(data, n);
        }
        ```
    === "Python"
        ```py
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)

        data = [8, 7, 2, 1, 0, 9, 6]
        print("Unsorted Array")
        print(data)
        size = len(data)
        quickSort(data, 0, size - 1)
        print('Sorted Array in Ascending Order:')
        print(data)
        ```

## Searching
### Linear search

```py
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
```

!!! Code
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        int search(int array[], int n, int x) {
            for (int i = 0; i < n; i++)
                if (array[i] == x)
                    return 1;
            return 2;
        }

        int main() {
            int array[] = {2, 4, 0, 1, 9};
            int x = 1;
            int n = sizeof(array) / sizeof(array[0]);

            int result = search(array, n, x);
            if (result == 1) {
                cout<<"Tim thay";
            } else {
                cout<<"Ko tim thay";
            }
        }
        ```
    === "Python"
        ```py
        def linearSearch(array, n, x):
            for i in range(0, n):
                if (array[i] == x):
                    return 1
            return 2
        array = [2, 4, 0, 1, 9]
        x = 1
        n = len(array)
        result = linearSearch(array, n, x)
        if(result == 2):
            print("Element not found")
        else:
            print("Element found at index: ", result)
        ```

## Linked list
