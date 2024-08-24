# Python language
<font size="1">[Programiz](https://www.programiz.com/python-programming){ .md-button }</font>
!!! info
    - For more:
        - [Library Functions](https://www.programiz.com/python-programming/methods)
        - [Built-in Functions](https://www.programiz.com/python-programming/methods/built-in/abs)
        - [List Methods](https://www.programiz.com/python-programming/methods/list/index)
        - [String Methods](https://www.programiz.com/python-programming/methods/string/capitalize)
        - [Set Methods](https://www.programiz.com/python-programming/methods/set/remove)
        - [Module Index](https://docs.python.org/3/py-modindex.html)

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

### Input & output

#### Input
```py
num = input('Enter a number: ')
print('You Entered:', num)
```

#### output
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
*output:*
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
*output:*
```
0
1
2
3
```

### While loop

```py
while condition:
    # body of while loop
```

### Bonus
#### Break
![alt text](<Screenshot 2024-08-24 at 15.45.06.png>)

```py
for i in range(5):
    if i == 3:
        break
    print(i)
```

*output:*

```
0
1
2
```


#### Continue
![alt text](<Screenshot 2024-08-24 at 15.45.51.png>)

```py
for i in range(5):
    if i == 3:
        continue
    print(i)
```

*output:*
```
0
1
2
4
```

#### Pass

```py
pass
```

## Data Types

| Data Types | Classes            | Description                             |
|:------------:|--------------------|-----------------------------------------|
| Numeric    | int, float, complex | holds numeric values                    |
| String     | str                | holds sequence of characters            |
| Sequence   | list, tuple, range | holds collection of items               |
| Mapping    | dict               | holds data in key-value pair form       |
| Boolean    | bool               | holds either `True` or `False`          |
| Set        | set, frozenset     | hold collection of unique items         |

E.g.

```py
num = int(input('Enter a number: '))
```

### List

E.g.
```py
languages = ['Python', 'Swift', 'C++']
print(languages[0])   # Python
print(languages[2])   # C++
```
E.g.
```py
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print(my_list[2:5]) # index 2 to index 4
print(my_list[5:])  # index 5 to end
print(my_list[:])   # items beginning to end
```

```
>> ['o', 'g', 'r']
>> ['a', 'm']
>> ['p', 'r', 'o', 'g', 'r', 'a', 'm']
```

- Change Items

```py
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)
colors[2] = 'Blue'
print('Updated List:', colors)
```

```
>> Original List: ['Red', 'Black', 'Green']
>> Updated List: ['Red', 'Black', 'Blue']
```

!!! tip
    - ``list()``: Convert to list
    ```py
    x = "axz"
    result = list(x)
    print(result)  
    ```
    ```
    >> ['a', 'x', 'z']
    ```

### String
E.g.
```py
greet = 'hello'
print(greet[1])    # "e"
print(greet[1:4])  # "ell"
```
E.g.
```py
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)
```
```
>> Never gonna give you up
>> Never gonna let you down
```
E.g.
```py
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')
```

```
>> Cathy is from UK
```

### Dictionary
```py
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])  # prints Kathmandu
print(capital_city['Kathmandu'])  # throws error message 
```

!!! note
    - Apply ``int()``, ``float()``, ``str()`` if and only if **explicit conversion**.
    - ``type()`` for checking data type.

## Random

```py
import random
```

| Function                         | Description                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| `seed(a=None, version=2)`        | Initialize the random number generator                                                          |
| `getstate()`                     | Returns an object capturing the current internal state of the generator                         |
| `setstate(state)`                | Restores the internal state of the generator                                                    |
| `getrandbits(k)`                 | Returns a Python integer with k random bits                                                     |
| `randrange(start, stop[, step])` | Returns a random integer from the range                                                         |
| `randint(a, b)`                  | Returns a random integer between a and b inclusive                                              |
| `choice(seq)`                    | Return a random element from the non-empty sequence                                             |
| `shuffle(seq)`                   | Shuffle the sequence                                                                            |
| `sample(population, k)`          | Return a k length list of unique elements chosen from the population sequence                   |
| `random()`                       | Return the next random floating point number in the range [0.0, 1.0)                            |
| `uniform(a, b)`                  | Return a random floating point number between a and b inclusive                                 |
| `triangular(low, high, mode)`    | Return a random floating point number between low and high, with the specified mode between those bounds |
| `betavariate(alpha, beta)`       | Beta distribution                                                                               |
| `expovariate(lambd)`             | Exponential distribution                                                                        |
| `gammavariate(alpha, beta)`      | Gamma distribution                                                                              |
| `gauss(mu, sigma)`               | Gaussian distribution                                                                           |
| `lognormvariate(mu, sigma)`      | Log normal distribution                                                                         |
| `normalvariate(mu, sigma)`       | Normal distribution                                                                             |
| `vonmisesvariate(mu, kappa)`     | Vonmises distribution                                                                           |
| `paretovariate(alpha)`           | Pareto distribution                                                                             |
| `weibullvariate(alpha, beta)`    | Weibull distribution                                                                            |

[For more](https://docs.python.org/3/library/random.html)

E.g.

```py
print(random.randrange(10, 20))
```
```
>> 15
```

E.g.

```py
list1 = ['a', 'b', 'c', 'd', 'e']
print(random.choice(list1))
random.shuffle(list1)
print(list1)
```
```
>> a
>> ['d', 'b', 'c', 'e', 'a']
```
E.g.
```py
print(random.random())
```
```
>> 0.6716121217631744
```

## Maths

```py
import math
```

| Function              | Description                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `ceil(x)`             | Returns the smallest integer greater than or equal to x.                                         |
| `copysign(x, y)`      | Returns x with the sign of y                                                                     |
| `fabs(x)`             | Returns the absolute value of x                                                                  |
| `factorial(x)`        | Returns the factorial of x                                                                       |
| `floor(x)`            | Returns the largest integer less than or equal to x                                              |
| `fmod(x, y)`          | Returns the remainder when x is divided by y                                                     |
| `frexp(x)`            | Returns the mantissa and exponent of x as the pair (m, e)                                        |
| `fsum(iterable)`      | Returns an accurate floating point sum of values in the iterable                                 |
| `isfinite(x)`         | Returns True if x is neither an infinity nor a NaN (Not a Number)                                |
| `isinf(x)`            | Returns True if x is a positive or negative infinity                                             |
| `isnan(x)`            | Returns True if x is a NaN                                                                       |
| `ldexp(x, i)`         | Returns x * (2**i)                                                                               |
| `modf(x)`             | Returns the fractional and integer parts of x                                                    |
| `trunc(x)`            | Returns the truncated integer value of x                                                         |
| `exp(x)`              | Returns e**x                                                                                     |
| `expm1(x)`            | Returns e**x - 1                                                                                 |
| `log(x[, b])`         | Returns the logarithm of x to the base b (defaults to e)                                         |
| `log1p(x)`            | Returns the natural logarithm of 1+x                                                             |
| `log2(x)`             | Returns the base-2 logarithm of x                                                                |
| `log10(x)`            | Returns the base-10 logarithm of x                                                               |
| `pow(x, y)`           | Returns x raised to the power y                                                                  |
| `sqrt(x)`             | Returns the square root of x                                                                     |
| `acos(x)`             | Returns the arc cosine of x                                                                      |
| `asin(x)`             | Returns the arc sine of x                                                                        |
| `atan(x)`             | Returns the arc tangent of x                                                                     |
| `atan2(y, x)`         | Returns atan(y / x)                                                                              |
| `cos(x)`              | Returns the cosine of x                                                                          |
| `hypot(x, y)`         | Returns the Euclidean norm, sqrt(x*x + y*y)                                                      |
| `sin(x)`              | Returns the sine of x                                                                            |
| `tan(x)`              | Returns the tangent of x                                                                         |
| `degrees(x)`          | Converts angle x from radians to degrees                                                         |
| `radians(x)`          | Converts angle x from degrees to radians                                                         |
| `acosh(x)`            | Returns the inverse hyperbolic cosine of x                                                       |
| `asinh(x)`            | Returns the inverse hyperbolic sine of x                                                         |
| `atanh(x)`            | Returns the inverse hyperbolic tangent of x                                                      |
| `cosh(x)`             | Returns the hyperbolic cosine of x                                                               |
| `sinh(x)`             | Returns the hyperbolic sine of x                                                                 |
| `tanh(x)`             | Returns the hyperbolic tangent of x                                                              |
| `erf(x)`              | Returns the error function at x                                                                  |
| `erfc(x)`             | Returns the complementary error function at x                                                    |
| `gamma(x)`            | Returns the Gamma function at x                                                                  |
| `lgamma(x)`           | Returns the natural logarithm of the absolute value of the Gamma function at x                   |
| `pi`                  | Mathematical constant, the ratio of circumference of a circle to its diameter (3.14159...)       |
| `e`                   | Mathematical constant e (2.71828...)                                                             |

[For more](https://docs.python.org/3/library/math.html)

E.g.

```py
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))
```
```
>> 3.141592653589793
>> -1.0
>> 22026.465794806718
>> 3.0
>> 1.1752011936438014
>> 720
```

## Functions
### Arguments
```py
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

add_numbers(5, 4)
```
```
>> Sum: 9
```
### Return
```py
def find_square(num):
    result = num * num
    return result

square = find_square(3)
print('Square:', square)
```
```
>> Square: 9
```
### Var Scope
#### Local
```py
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
print(message)
```
#### Global

```py
message = 'Hello'           # declare global variable

def greet():
    print('Local', message) # declare local variable

greet()
print('Global', message)
```

- Keyword

```py
c = 1           # global variable

def add():
    global c    # use of global keyword
    c = c + 2 
    print(c)

add()
```
```
>> 3 
```

#### Nonlocal

```py
def outer():
    message = 'local'

    def inner():
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
```
```
>> inner: nonlocal
>> outer: nonlocal
```

### Recursion

```py
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))
```

```
>> The factorial of 3 is 6
```

### Modules

```py
# stored in file: example.py
def add(a, b):
   result = a + b
   return result
```

- At another file

```py
import example
example.add(4,5) # returns 9
```

**Standard**

```py
import math
print("The value of pi is", math.pi)
```

```
>> The value of pi is 3.141592653589793
```

!!! tip
    - Import with renaming
    ```py
    import math as m
    print(m.pi) # Output: 3.141592653589793
    ```
    - Import specific names from a module without importing the module as a whole
    ```py
    from math import pi
    print(pi) # Output: 3.141592653589793
    ```
    - Import all names (definitions) from a module
    ```py
    from math import *
    print("The value of pi is", pi)
    ```

### Package

![alt text](<Screenshot 2024-08-24 at 21.48.56.png>)

- Initialization file: ``__init__.py``

```py
import Game.Level.start
Game.Level.start.select_difficulty(2)
```

```py
from Game.Level import start
start.select_difficulty(2)
```

```py
from Game.Level.start import select_difficulty
select_difficulty(2)
```




