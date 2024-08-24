# Python language
## Comments

```py
# Bancie
``` 

!!! tip
    command + /

```py
'''
bancie
banciee
bancieee
'''
```

## Fundementals
### Variable
```py
a, b, c = 5, 3.2, 'Hello'
print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello 
```

```py
site1 = site2  = 'programiz.com'
print (x)  # prints programiz.com
print (y)  # prints programiz.com
```
### Data type

| Data Types | Classes            | Description                             |
|:------------:|--------------------|-----------------------------------------|
| Numeric    | int, float, complex | holds numeric values                    |
| String     | str                | holds sequence of characters            |
| Sequence   | list, tuple, range | holds collection of items               |
| Mapping    | dict               | holds data in key-value pair form       |
| Boolean    | bool               | holds either `True` or `False`          |
| Set        | set, frozenset     | hold collection of unique items         |

```py
num = int(input('Enter a number: '))
```
#### Tuple Items
```py
languages = ["Swift", "Java", "Python"]
print(languages[0])
print(languages[2])
>>> Swift
>>> Python
```
#### Dictionary
```py
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])  # prints Kathmandu
print(capital_city['Kathmandu'])  # throws error message 
```

!!! note
    - Apply ``int()``, ``float()``, ``str()`` if and only if **explicit conversion**.
    - ``type()`` for checking data type.

### Input & Output

#### Input
```py
num = input('Enter a number: ')
print('You Entered:', num)
```

#### Output
```py
print('Programiz is ' + 'awesome.')
>>> Programiz is awesome.
```

```py
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))
>>> The value of x is 5 and y is 10
```

### Operators

| Operator | Operation      | Example       |
|:----------:|----------------|---------------|
| `+`      | Addition       | `5 + 2 = 7`   |
| `-`      | Subtraction    | `4 - 2 = 2`   |
| `*`      | Multiplication | `2 * 3 = 6`   |
| `/`      | Division       | `4 / 2 = 2`   |
| `//`     | Floor Division | `10 // 3 = 3` |
| `%`      | Modulo         | `5 % 2 = 1`   |
| `**`     | Power          | `4 ** 2 = 16` |

**Assignment**

| Operator | Name                    | Example                |
|:----------:|-------------------------|------------------------|
| `=`      | Assignment Operator      | `a = 7`                |
| `+=`     | Addition Assignment      | `a += 1  # a = a + 1`  |
| `-=`     | Subtraction Assignment   | `a -= 3  # a = a - 3`  |
| `*=`     | Multiplication Assignment| `a *= 4  # a = a * 4`  |
| `/=`     | Division Assignment      | `a /= 3  # a = a / 3`  |
| `%=`     | Remainder Assignment     | `a %= 10 # a = a % 10` |
| `**=`    | Exponent Assignment      | `a **= 10 # a = a ** 10` |

**Logical**

| Operator | Example   | Meaning                                      |
|:----------:|-----------|----------------------------------------------|
| `and`    | `a and b` | **Logical AND:** `True` only if both operands are `True` |
| `or`     | `a or b`  | **Logical OR:** `True` if at least one operand is `True` |
| `not`    | `not a`   | **Logical NOT:** `True` if the operand is `False` and vice-versa. |

**Special**

| Operator  | Meaning                                                                     | Example      |
|:-----------:|-----------------------------------------------------------------------------|--------------|
| `is`      | `True` if the operands are identical (refer to the same object)             | `x is True`  |
| `is not`  | `True` if the operands are not identical (do not refer to the same object)  | `x is not True` |
| `in`      | `True` if value/variable is **found** in the sequence        | `5 in x`     |
| `not in`  | `True` if value/variable is **not found** in the sequence    | `5 not in x` |

```py
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False
```

```py
message = 'Hello world'
dict1 = {1:'a', 2:'b'}
print('H' in message)  # prints True
print('hello' not in message)  # prints True
print(1 in dict1)  # prints True
print('a' in dict1)  # prints False
```

## Flow Control
### If else
```py
if condition:
    # body of if statement
```

e.g.

```py
number = int(input('Enter a number: '))
if number > 0:
    print(f'{number} is a positive number.')
print('A statement outside the if statement.')
```
output:
```
Enter a number: 10
10 is a positive number.
A statement outside the if statement.
```
```
Enter a number: -2
A statement outside the if statement.
```

!!! note
    Python uses **indentation** to define a block of code, such as the body of an if statement.

```py
if condition:
    # body of if statement
else:
    # body of else statement
```

```py
if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
```

### For loop

```py
for val in sequence:
    # body of the loop
```

e.g.

```py
languages = ['Swift', 'Python', 'Go']
for x in languages:
    print(x)
>> Swift
>> Python
>> Go
```

#### range()
```py
for i in range(4):
    print(i)
```
output
```
0
1
2
3
```