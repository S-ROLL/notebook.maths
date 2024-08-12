## Introduction

### Chú thích

- ``//`` : cmt.
- ``/* ... */`` : cmt.

### Nhập/xuất dữ liệu

- ``cin >>`` : Nhập dữ liệu.
- ``cout <<`` : Xuất dữ liệu.

### Kiểu dữ liệu

- **Integer**
    - ``unsigned int`` : $0\rightarrow 65535$ *(16 bits)*.
    - ``int`` : $-32768 \rightarrow 32767$ *(16 bits)*.
    - ``unsigned long`` : $0 \rightarrow 4294967295$ *(32 bits)*.
    - ``long`` : $-2147483648 \rightarrow 2147483647$ *(32 bits)*.
- **Real**
    - ``float`` : $3.4 \times 10^{-38} \rightarrow 3.4 \times 10^{38}$ *(32 bits)*.
    - ``double`` : $1.7\times 10^{-308} \rightarrow 1.7 \times 10^{308}$ *(64 bits)*.
    - ``long double`` : $3.4 \times 10^{-4932} \rightarrow 1.1 \times 10^{4932}$ *(80 bits)*.

> Hàm ``sizeof(__)`` sẽ cho biết mỗi biến chiếm bao nhiêu byte bộ nhớ.

- **Chuyển đổi kiểu dữ liệu** (Ex. ``int a,b`` sang ``a/b``):
    - ``(float)a/b``
    - ``float(a)/b``
    - ``a/float(b)``

> ``a`` or ``b`` constant $\rightarrow$ ``1.0/b``

### Khai báo

- **Variable**: ``Kiểu dữ liệu <biến>;``
    - ``int a,b,c;``
- **Constant**
    - ``#define a 4``
    - ``const int a=4;``
> a: name constant, 4: value constant

### Standard function

- ``sqrt(a)`` : $\sqrt{a}$
- ``pow(a,b)`` : $a^b$
- ``abs(a)`` : $|a|$

### Toán tử

- **Chia dư**
    - $a=nq+r$ (a: số bị chia, n: số chia, q: thương, r: số dư)

- **So sánh**
    - ``<``, ``>`` : nhỏ hơn, lớn hơn.
    - ``==``,``!=`` : bằng, khác.
    - ``<=``, ``>=`` : nhỏ hơn hoặc bằng, lớn hơn hoặc bằng.
- **Logic**

| a | b | !a | a $\parallel$ b | a && b |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 |

> - ``||`` : OR
> - ``&&`` : AND 
- **Tăng/giảm**
    - ``++a`` : a tăng 1 đơn vị trước khi tính.
    - ``a++`` : a tăng 1 đơn vị sau khi được tính.
    - ``--a`` : a giảm 1 đơn vị trước khi tính.
    - ``a--`` : a giảm 1 đơn vị trước khi tính.
- **Điều kiện** : ``<ĐK> ? <1> : <2>``
    - ``<ĐK>`` : True $\rightarrow$ ``<1>``
    - ``<ĐK>`` : False $\rightarrow$ ``<2>``

## Flow Control
### Condition
#### if

```cpp
if (condition) {
  // body;
}
```

0. **Start.**
1. ``condition`` :
      - If ``condition`` : ``true`` $\rightarrow$ ``body`` is executed $\rightarrow$ 2.
      - If ``condition`` : ``false`` $\rightarrow$ ``body`` is skipped $\rightarrow$ 2.
2. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.06.39.png>)

#### if...else

```cpp
if (condition) {
  // code_1;
}
else {
  // code_2;
}
```

0. **Start.**
1. ``condition`` :
      - If the ``condition`` : ``true`` $\rightarrow$ ``code_1`` is executed $\rightarrow$ 2.
      - If the ``condition`` : ``false`` $\rightarrow$ ``code_2`` is executed $\rightarrow$ 2.
2. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.08.01.png>)

#### if...else...else if

```cpp
if (condition1) {
  // code_1;
}
else if (condition2){
  // code_2;
}
else {
  // code_3;
}
```

0. **Start.**
1. ``condition1`` :
      - If ``condition1`` : ``true`` $\rightarrow$ ``code_1`` is executed $\rightarrow$ 3.
      - If ``condition1`` : ``false`` $\rightarrow$ 2.
2. ``condition2`` :
      - If ``condition2`` : ``true`` $\rightarrow$ ``code_2`` is executed $\rightarrow$ 3.
      - If ``condition2`` : ``false`` $\rightarrow$ ``code_3`` is executed $\rightarrow$ 3.
3. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.08.40.png>)
### switch case

```cpp
switch (expression)  {
    case 'constant1':
        // body that expression is equal to constant1;
        break;

    case 'constant2':
        // body that expression is equal to constant2;
        break;
        .
        .
        .
    default:
        // body_default
}
```

0. **Start.**
1. ``expression`` :
      - If ``expression`` : ``match`` $\rightarrow$ ``body matched`` is executed $\rightarrow$ 2.
      - If ``expression`` : ``no match`` $\rightarrow$ ``body_default`` is executed $\rightarrow$ 2.
2. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.10.43.png>)

### LOOP

#### for

```cpp
for (initialization; condition; update) {
    // body;
}
```

0. **Start.**
1. ``initialization``
2. ``condition`` :
      - If ``condition`` : ``true`` $\rightarrow$ ``body`` is executed $\rightarrow$ 3.
      - If ``condition`` : ``false`` $\rightarrow$ ``body`` is terminated $\rightarrow$ 4.
3. ``update`` $\rightarrow$ 2.
4. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.13.15.png>)

#### for (arrays & vectors)

```cpp
for (variable : collection) {
    // body;
}
```

#### while

```cpp
while (condition) {
    // body;
}
```

0. **Start.**
1. ``condition`` :
      - if ``condition`` : ``true`` $\rightarrow$ ``body`` is executed $\rightarrow$ 1.
      - if ``condition`` : ``false`` $\rightarrow$ 2.
2. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.14.29.png>)

#### do while

```cpp
do {
   // body;
}
while (condition);
```

0. **Start.**
1. ``body``
2. ``condition`` :
      - If ``condition`` : ``true`` $\rightarrow$ 1.
      - If ``condition`` : ``false`` $\rightarrow$ 3.
3. **Terminate.**

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.15.15.png>)

## Syntax

- ``break;``

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.16.01.png>)

- ``continue;``

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.16.21.png>)

- ``goto``

```cpp
goto //label;
...
//label:
//code block;
```

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.17.05.png>)

## Functions

- How it works / Parameters / Return statement

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.17.48.png>)

### 4 Methods:
#### 1. No arguments, no return

```cpp
void prime();
int main() {
    prime();
    return 0;
}
void prime() {
    int num, i, flag = 0;
    cout << "Enter a positive integer enter to check: ";
    cin >> num;
    for(i = 2; i <= num/2; i++) {
        if(num % i == 0) {
            flag = 1; 
            break;
        }
    }
    if (flag == 1) {
        cout << num << " is not a prime number.";
    } else {
        cout << num << " is a prime number.";
    }
}
```

#### 2. No arguments, return

```cpp
int prime();
int main() {
    int num, i, flag = 0;
    num = prime();
    for (i = 2; i <= num/2; ++i) {
        if (num%i == 0) {
            flag = 1;
            break;
        }
    }
    if (flag == 1) {
        cout<<num<<" is not a prime number.";
    } else {
        cout<<num<<" is a prime number.";
    }
    return 0;
}
int prime() {
    int n;
    printf("Enter a positive integer to check: ");
    cin >> n;
    return n;
}
```

#### 3. Arguments, no return

```cpp
void prime(int n);
int main() {
    int num;
    cout << "Enter a positive integer to check: ";
    cin >> num;
    prime(num);
    return 0;
}
void prime(int n) {
    int i, flag = 0;
    for (i = 2; i <= n/2; ++i) {
        if (n%i == 0) {
            flag = 1;
            break;
        }
    }
    if (flag == 1) {
        cout << n << " is not a prime number.";
    } else {
        cout << n << " is a prime number.";
    }
}
```

#### 4. Arguments, return

```cpp
int prime(int n);
int main() {
    int num, flag = 0;
    cout << "Enter positive integer to check: ";
    cin >> num;
    flag = prime(num);
    if (flag == 1) {
        cout << num << " is not a prime number.";
    } else {
        cout<< num << " is a prime number.";
    }
    return 0;
}
int prime(int n) {
    for (int i = 2; i <= n/2; ++i) {
        if (n % i == 0) {
            return 1;
        }
    }
    return 0;
}
```

### Overloading
#### Different Number & Type

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.19.46.png>)

### Default arguments

![alt text](<cpp lib/Screenshot 2024-08-03 at 21.20.31.png>)

> Once we provide a default value for a parameter, all subsequent parameters must also have default values.

```cpp
// Invalid
void add(int a, int b = 3, int c, int d);
// Invalid
void add(int a, int b = 3, int c, int d = 4);
// Valid
void add(int a, int c, int b = 3, int d = 4);
```

### Storage Class

- Local Variable

```cpp
void test();
int main()  {
    int var = 5;
    test();
    var1 = 9;
}
void test() {
    int var1;
    var1 = 6;
    cout << var;
}
```

- Global Variable

```cpp
int c = 12;
void test();
int main() {
    ++c;
    cout << c <<endl;
    test();
    return 0;
}
void test() {
    ++c;
    cout << c;
}
```

- Static Local variable

```cpp
void test() {
    static int var = 0;
    ++var;
    cout << var << endl;
}
int main() {
    test();
    test();
    return 0;
}
```
``output: 1 2`` instead of ``1 1``.

## Arrays