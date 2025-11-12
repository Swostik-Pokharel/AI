#programming #python 
I guess we always start with :
```python
print("hello world")
```

## Variables
The basic is that we use stuff to keep values in and that stuff is called a variable . for eg :
```python 
print ("hello hero?")
print ("how are you hero?")
print ("how old are you hero?")
```
where we explicitly tell the name of the person everytime,A better approach is :
```python 
user ="hero" 
print(f"hello {user}?" )
print(f"how are you {user}?" )
print (f"how old are you {user}")
```
now you can change the user name in one place and everything will update accordingly . Additionally what this then lets us do is the following:
```python 
user =input("enter your name")
print(f"hello {user}?" )
print(f"how are you {user}?" )
print (f"how old are you {user}")
```
where now when you run it it become something like :
```python
enter your name 
Swostik #enter 

hello swostik ?
how are you swostik ?
how old are you swostik ?
```

That is why we need variable , a key thing to consider is that the more variables you have the more memory your program requires . Although this is not super relevant just yet its a useful thing to keep i the back of your mind while solving problems , usually its better to solve problems with as few variables as you can . (Also keeping readability in mind )

## Basic data types :
The **basic data types** in Python are:

**Numeric Types**

- `int` (integer) - whole numbers like `42`, `-10`, `0`
- `float` (floating-point) - decimal numbers like `3.14`, `-0.5`, `2.0`
- `complex` - complex numbers like `3+4j`, `2-5j`

**Text Type**

- `str` (string) - text enclosed in quotes like `"hello"`, `'Python'`

**Boolean Type**

- `bool` (boolean) - logical values `True` or `False`

**None Type**

- `NoneType` - represents the absence of a value, written as `None`

### Python Operators Guide

#### 1. Arithmetic Operators

Used for mathematical operations.

|Operator|Description|Example|Result|
|---|---|---|---|
|`+`|Addition|`5 + 3`|`8`|
|`-`|Subtraction|`10 - 4`|`6`|
|`*`|Multiplication|`3 * 4`|`12`|
|`/`|Division|`15 / 2`|`7.5`|
|`//`|Floor Division|`15 // 2`|`7`|
|`%`|Modulus (remainder)|`17 % 5`|`2`|
|`**`|Exponentiation|`2 ** 3`|`8`|

#### 2. Comparison Operators

Used to compare values, returns `True` or `False`.

| Operator | Description           | Example  | Result |
| -------- | --------------------- | -------- | ------ |
|  ==      | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 3` | `True` |
| `>`      | Greater than          | `7 > 5`  | `True` |
| `<`      | Less than             | `3 < 5`  | `True` |
| `>=`     | Greater than or equal | `5 >= 5` | `True` |
| `<=`     | Less than or equal    | `4 <= 5` | `True` |

#### 3. Logical Operators

Used to combine conditional statements.

| Operator | Description                          | Example          | Result  |
| -------- | ------------------------------------ | ---------------- | ------- |
| `and`    | Returns True if both are true        | `True and False` | `False` |
| `or`     | Returns True if at least one is true | `True or False`  | `True`  |
| `not`    | Reverses the boolean value           | `not True`       | `False` |
|          |                                      |                  |         |

**Example:**

```python
age = 25
has_license = True

# Can drive if age >= 18 AND has license
can_drive = age >= 18 and has_license  # True
```

#### 4. Assignment Operators

Used to assign values to variables.

|Operator|Example|Equivalent To|
|---|---|---|
|`=`|`x = 5`|`x = 5`|
|`+=`|`x += 3`|`x = x + 3`|
|`-=`|`x -= 2`|`x = x - 2`|
|`*=`|`x *= 4`|`x = x * 4`|
|`/=`|`x /= 2`|`x = x / 2`|
|`//=`|`x //= 2`|`x = x // 2`|
|`%=`|`x %= 3`|`x = x % 3`|
|`**=`|`x **= 2`|`x = x ** 2`|

#### 5. Identity Operators

Check if objects are the same (same memory location).

|Operator|Description|Example|
|---|---|---|
|`is`|Returns True if both refer to same object|`x is y`|
|`is not`|Returns True if both refer to different objects|`x is not y`|

**Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same values)
print(a is b)   # False (different objects)
print(a is c)   # True (same object)
```

#### 6. Membership Operators

Check if a value exists in a sequence.

|Operator|Description|Example|
|---|---|---|
|`in`|Returns True if value exists in sequence|`'a' in 'cat'`|
|`not in`|Returns True if value doesn't exist|`'x' not in 'cat'`|

**Example:**

```python
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)      # True
print('grape' not in fruits)  # True
```

#### 7. Bitwise Operators

Operate on binary representations of numbers.

|Operator|Description|Example|
|---|---|---|
|`&`|AND|`5 & 3` → `1`|
|`\|`|OR|`5 \| 3` → `7`|
|`^`|XOR|`5 ^ 3` → `6`|
|`~`|NOT|`~5` → `-6`|
|`<<`|Left shift|`5 << 1` → `10`|
|`>>`|Right shift|`5 >> 1` → `2`|

**Example:**

```python
# 5 in binary: 101
# 3 in binary: 011

print(5 & 3)   # 1 (binary: 001)
print(5 | 3)   # 7 (binary: 111)
```

#### Operator Precedence

When multiple operators appear in an expression, Python follows this order (highest to lowest):

1. `**` (Exponentiation)
2. `~`, `+`, `-` (Unary operators)
3. `*`, `/`, `//`, `%` (Multiplication, Division)
4. `+`, `-` (Addition, Subtraction)
5. `<<`, `>>` (Bitwise shifts)
6. `&` (Bitwise AND)
7. `^` (Bitwise XOR)
8. `|` (Bitwise OR)
9. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` (Comparisons)
10. `not` (Logical NOT)
11. `and` (Logical AND)
12. `or` (Logical OR)

**Use parentheses `()` to make precedence explicit!**

```python
result = 2 + 3 * 4      # 14 (multiplication first)
result = (2 + 3) * 4    # 20 (parentheses first)
```
