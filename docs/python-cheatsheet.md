# Python Cheat Sheet

## Variables & Data Types

```python
# Variables (no declaration needed)
x = 10
name = "Alice"
pi = 3.14
is_active = True

# Basic types
type(x)  # <class 'int'>
isinstance(x, int)  # True

# Type conversion
int("42")  # 42
str(42)  # "42"
float(42)  # 42.0
bool(1)  # True
list("abc")  # ['a', 'b', 'c']
```

## Strings

```python
# String creation
s = "hello"
s = 'hello'
s = """multi
line"""

# String operations
len(s)  # length
s.upper()  # "HELLO"
s.lower()  # "hello"
s.strip()  # remove whitespace
s.split(',')  # split by delimiter
s.replace('e', 'a')  # replace
s.find('l')  # find index
s.startswith('he')  # True
s.endswith('o')  # True
' '.join(['a', 'b', 'c'])  # "a b c"

# String formatting
f"Hello {name}"  # f-string (Python 3.6+)
"Hello {}".format(name)  # format()
"Hello %s" % name  # old-style

# String slicing
s[0]  # first char
s[-1]  # last char
s[1:3]  # "el"
s[::2]  # every 2nd char
s[::-1]  # reverse
```

## Lists

```python
# Create
lst = [1, 2, 3]
lst = list()
lst = [x for x in range(5)]  # [0, 1, 2, 3, 4]

# Access
lst[0]  # first element
lst[-1]  # last element
lst[1:3]  # slice [2, 3]

# Modify
lst.append(4)  # add to end
lst.insert(0, 0)  # insert at index
lst.extend([5, 6])  # add multiple
lst.remove(2)  # remove by value
lst.pop()  # remove & return last
lst.pop(0)  # remove at index
lst.clear()  # empty list
del lst[0]  # delete by index

# Query
len(lst)  # length
2 in lst  # membership
lst.index(2)  # find index
lst.count(2)  # count occurrences
lst.sort()  # sort in-place
sorted(lst)  # return sorted copy
lst.reverse()  # reverse in-place
```

## Tuples

```python
# Immutable lists
t = (1, 2, 3)
t = tuple([1, 2, 3])

# Access (same as lists)
t[0]  # 1
t[1:3]  # (2, 3)

# Unpacking
a, b, c = (1, 2, 3)
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2,3,4]
```

## Dictionaries

```python
# Create
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)
d = {k: v for k, v in zip(['a', 'b'], [1, 2])}

# Access
d['a']  # 1
d.get('a')  # 1
d.get('c', 0)  # 0 (default)

# Modify
d['c'] = 3  # add/update
d.update({'d': 4})  # merge
d.pop('a')  # remove & return
d.clear()  # empty

# Query
len(d)  # number of items
'a' in d  # True
d.keys()  # dict_keys(['a', 'b'])
d.values()  # dict_values([1, 2])
d.items()  # dict_items([('a', 1), ('b', 2)])
```

## Sets

```python
# Create (unordered, unique)
s = {1, 2, 3}
s = set()
s = set([1, 2, 2, 3])  # {1, 2, 3}

# Modify
s.add(4)  # add element
s.remove(2)  # remove or KeyError
s.discard(2)  # remove silently
s.pop()  # remove & return
s.clear()  # empty

# Operations
s1 | s2  # union
s1 & s2  # intersection
s1 - s2  # difference
s1 ^ s2  # symmetric difference
s1.issubset(s2)  # s1 ⊆ s2
s1.issuperset(s2)  # s1 ⊇ s2
```

## Control Flow

```python
# if/elif/else
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Ternary
result = "yes" if x > 0 else "no"

# for loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for item in lst:
    print(item)

for i, item in enumerate(lst):
    print(i, item)

for k, v in d.items():
    print(k, v)

# while loop
while x > 0:
    x -= 1

# break/continue
for i in range(10):
    if i == 5:
        break  # exit loop
    if i == 2:
        continue  # skip iteration
```

## Functions

```python
# Define
def greet(name):
    return f"Hello {name}"

def add(a, b=0):  # default argument
    return a + b

def multiply(*args):  # variable positional
    result = 1
    for x in args:
        result *= x
    return result

def config(**kwargs):  # variable keyword
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2
square(5)  # 25

# Map, filter, reduce
list(map(square, [1, 2, 3]))  # [1, 4, 9]
list(filter(lambda x: x > 2, [1, 2, 3]))  # [3]

from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10
```

## Exception Handling

```python
# try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error")
finally:
    print("Always runs")

# Raise
if x < 0:
    raise ValueError("x must be positive")
```

## File Operations

```python
# Read
with open('file.txt', 'r') as f:
    content = f.read()  # whole file
    lines = f.readlines()  # list of lines

# Write
with open('file.txt', 'w') as f:
    f.write("Hello")
    f.writelines(['line1', 'line2'])

# Append
with open('file.txt', 'a') as f:
    f.write("More")

# JSON
import json
json.dumps(d)  # dict -> string
json.loads(s)  # string -> dict
json.dump(d, f)  # dict -> file
json.load(f)  # file -> dict
```

## List Comprehensions

```python
# Basic
[x for x in range(5)]  # [0, 1, 2, 3, 4]
[x*2 for x in range(5)]  # [0, 2, 4, 6, 8]

# With condition
[x for x in range(10) if x % 2 == 0]  # evens

# Nested
[[x+y for x in [1,2]] for y in [10,20]]  # [[11,12],[21,22]]

# Dict comprehension
{x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, ...}

# Set comprehension
{x % 2 for x in range(5)}  # {0, 1}
```

## Common Built-ins

```python
# Iteration
range(5)  # 0, 1, 2, 3, 4
enumerate([a, b, c])  # (0,a), (1,b), (2,c)
zip([1,2], ['a','b'])  # (1,'a'), (2,'b')
reversed([1, 2, 3])  # 3, 2, 1

# Aggregation
sum([1, 2, 3])  # 6
min([3, 1, 2])  # 1
max([3, 1, 2])  # 3
len([1, 2, 3])  # 3
all([True, True])  # True
any([False, True])  # True

# Sorting & ordering
sorted([3, 1, 2])  # [1, 2, 3]
sorted(lst, reverse=True)
sorted(lst, key=lambda x: x[1])  # sort by 2nd element

# Type checks
type(x)
isinstance(x, int)
callable(func)
```

## Common Modules

```python
# Math
import math
math.sqrt(16)  # 4.0
math.ceil(4.3)  # 5
math.floor(4.7)  # 4
math.pi, math.e

# Random
import random
random.randint(1, 10)  # 1-10
random.choice([1, 2, 3])
random.shuffle(lst)  # in-place
random.sample(lst, 2)  # 2 random items

# Datetime
from datetime import datetime, timedelta
now = datetime.now()
now.year, now.month, now.day
delta = timedelta(days=1)
tomorrow = now + delta

# OS/Path
import os
os.path.exists('file.txt')
os.path.join('folder', 'file.txt')
import pathlib
p = pathlib.Path('file.txt')

# Itertools
from itertools import combinations, permutations
combinations([1,2,3], 2)  # (1,2), (1,3), (2,3)
```

## Classes & OOP

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} barks"
    
    @staticmethod
    def species():
        return "Canis familiaris"
    
    @classmethod
    def from_string(cls, s):
        return cls(s)

dog = Dog("Rex")
dog.bark()  # "Rex barks"
Dog.species()  # "Canis familiaris"

# Inheritance
class Animal:
    def speak(self):
        return "Sound"

class Cat(Animal):
    def speak(self):
        return "Meow"
```

## String Methods Cheat Sheet

```python
s = "Hello World"

s.capitalize()  # "Hello world"
s.upper()  # "HELLO WORLD"
s.lower()  # "hello world"
s.title()  # "Hello World"
s.swapcase()  # "hELLO wORLD"

s.count('l')  # 3
s.find('World')  # 6 (-1 if not found)
s.replace('World', 'Python')  # "Hello Python"

s.split()  # ["Hello", "World"]
' '.join(["Hello", "World"])  # "Hello World"
s.strip()  # remove leading/trailing whitespace

s.startswith('Hello')  # True
s.endswith('World')  # True
s.isdigit()  # False
s.isalpha()  # False
s.isalnum()  # False
```

## Common Patterns

```python
# Iterating with index
for i, item in enumerate(lst):
    print(i, item)

# Multiple assignment
a, b = 1, 2

# Swapping
a, b = b, a

# Default dict
from collections import defaultdict
d = defaultdict(list)
d[key].append(value)

# Counter
from collections import Counter
c = Counter(['a', 'b', 'a'])  # Counter({'a': 2, 'b': 1})

# Assertion
assert x > 0, "x must be positive"

# Pass statement (placeholder)
def todo():
    pass
```

## Tips & Tricks

```python
# Check if list is empty
if lst:  # True if not empty
    pass

# Multiple conditions
if x > 0 and x < 10:
    pass

# Check membership
if item in lst:
    pass

# Get with default
d.get(key, default_value)

# None checks
if x is None:
    pass

# Walrus operator (Python 3.8+)
if (n := len(lst)) > 5:
    print(f"List has {n} items")
```
