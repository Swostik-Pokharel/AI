#programming #python 
## Conditionals 
Simply  speaking conditionals help us determine if any given condition is met so we can can then take the next step accordingly . There are basically 3 main conditionals `if`
,`else` and `elif` which will be demonstrated by the following classic example :

```python 
order = input("""Menu: 
1. Burger 
2. Fries 
3. Milk """)
if order is "Burger":
	print ("pay 10$)
elif order is "fries":
	print ("Pay 5$") 
else :
print ("pay 2$")

```

Diagram example :
![[conditionals.png|500x500]]
## What Are Iterables?

An **iterable** is any Python object you can loop through, one item at a time.

**Common iterables:**

|Type|Example|Loops Through|
|---|---|---|
|**String**|`"hello"`|`'h'`, `'e'`, `'l'`, `'l'`, `'o'`|
|**List**|`[1, 2, 3]`|`1`, `2`, `3`|
|**Tuple**|`(1, 2, 3)`|`1`, `2`, `3`|
|**Dictionary**|`{'a': 1}`|Keys: `'a'`|
|**Set**|`{1, 2, 3}`|`1`, `2`, `3`|
|**Range**|`range(5)`|`0`, `1`, `2`, `3`, `4`|

**Key point:** If you can use it in a `for` loop, it's an iterable!

---

## 1. `for` Loop

Used to iterate over an iterable (sequence like list, tuple, string, range, etc.).

### Basic Syntax

python

```python
for item in sequence:
    # code to execute
```

### Examples

**Looping through a list:**

python

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

**Using `range()`:**

python

```python
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# range(start, stop, step)
for i in range(2, 10, 2):
    print(i)  # Prints 2, 4, 6, 8
```

**Using `enumerate()` (get index and value):**

python

```python
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"{index}: {color}")# 0:red 1:green 2:blue
```

## 2. `while` Loop

Repeats as long as a condition is `True`.

### Basic Syntax

python

```python
while condition:
    # code to execute
```

### Examples

**Basic while loop:**

python

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**User input loop:**

python

```python
password = ""
secret="12345"
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

**Infinite loop (be careful!):**
```python
# This runs forever unless you break it
while True:
    response = input("Type 'quit' to exit: ")
    if response == 'quit':
        break
```

## 3. Loop Control Statements

### `break` - Exit the loop immediately

python

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4
```

### `continue` - Skip to next iteration

python

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4 (skips 2)
```

### `pass` - Do nothing (placeholder)

python

```python
for i in range(5):
    if i == 2:
        pass
    print(i)  # Prints all: 0, 1, 2, 3, 4
```

## 4. Nested Loops

A **nested loop** is a loop inside another loop. The inner loop completes all its iterations for each single iteration of the outer loop.

python

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

**Step-by-step execution:**

1. `i=0`: Inner loop runs completely → `j=0`, then `j=1`
2. `i=1`: Inner loop runs completely → `j=0`, then `j=1`
3. `i=2`: Inner loop runs completely → `j=0`, then `j=1`

**Output:**

```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

**Total iterations:** 3 × 2 = 6

## 5. `else` with Loops

The `else` block runs when the loop completes normally (not broken by `break`).

### With `for` loop:

python

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

### With `break`:

python

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")  # Won't run because of break
```

### Practical use - Searching:

python

```python
numbers = [1, 3, 5, 7, 9]
search = 4

for num in numbers:
    if num == search:
        print("Found!")
        break
else:
    print("Not found!")
```

## Common Patterns

## `for` vs `while`

| Use `for` when...                    | Use `while` when...                           |
| ------------------------------------ | --------------------------------------------- |
| You know how many iterations         | You don't know how many iterations            |
| Iterating over a sequence            | Waiting for a condition to change             |
| Processing each item in a collection | Creating infinite loops with break conditions |

**Example:**
```python
# for - known iterations
for i in range(10):
    print(i)

# while - unknown iterations
while user_input != "quit":
    user_input = input("Enter command: ")
```


