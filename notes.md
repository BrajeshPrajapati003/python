## 🧠 What is .venv

.venv = Virtual Environment

In simple terms:
A private Python universe for ONE project.
- It’s a self-contained folder that holds:
- its own python.exe
- its own pip
- its own installed libraries (like black, numpy, etc.)

![.venv analogy](<notes img/image.png>)

You NEVER edit anything inside .venv manually.

It’s managed by Python tooling.

```python 
python -m venv .venv
pip install -r requirements.txt
```
That's how real projects scale.


## ✅ Python List Functions & Operations

🔹 Adding Elements

- append(x) → adds one element at the end
- extend(iterable) → adds elements one by one from another iterable
- insert(i, x) → inserts at a specific index (shifts elements right)

🔹 Removing Elements

- remove(x) → removes the first occurrence of a value
- pop() → removes & returns last element
- pop(i) → removes & returns element at index i
- clear() → removes all elements

🔹 Searching & Counting

- index(x) → returns index of first occurrence
- count(x) → counts occurrences of a value

🔹 Sorting & Reversing

- sort() → sorts list in ascending order
- sort(reverse=True) → descending order
- reverse() → reverses list in-place

🔹 Built-in Utility Functions

- len(list) → number of elements
- min(list) → smallest element
- max(list) → largest element

🔹 Copying Lists

- copy() → shallow copy
- list[:] → slicing copy
- list(a) → constructor copy

⚠️ b = a → not a copy, just a reference (classic interview trap)

🔹 Indexing Tricks

- Positive indexing → starts from 0
- Negative indexing → starts from -1 (last element)
  
```python
a = [10, 20, 30]
a[-1]  # 30
a[-2]  # 20
```

🔹 Slicing (Power Feature 💪)

a[start : end : step]

Examples:

```python
a[1:4]     # sublist
a[::-1]    # reverse list
a[:3]      # first 3 elements
a[::2]     # every alternate element
```

🎯 Pro Tips

- append() is O(1), insert() is O(n)
- remove() fails if element not found → raises ValueError
- sort() modifies list; sorted() returns a new one
- Lists are mutable (contrast with tuples)


## 📌 Python List Copy vs Java Copy — Quick Notes
🔹 Assignment (Python & Java)

Copies reference only
No new object created
Changes reflect everywhere

**Python**
```
b = a
```
**Java**
```
List<Integer> b = a;
```

🔹 Shallow Copy (Container copied, elements shared)

**✅ Python**
```
b = a.copy()
# or
b = a[:]
```

- New list object created
- Elements’ references are reused
- Safe for immutable elements
- Unsafe for nested mutable objects

**✅ Java (Equivalent)**
```
List<Integer> b = new ArrayList<>(a);
```

- Same behavior as Python copy()
- New list, same element references


🔹 Deep Copy (Everything copied)

**Python**
```Python
import copy
b = copy.deepcopy(a)
```

- New container
- New inner objects
- No shared state

**Java**

- No built-in deep copy
- Must be done manually (copy constructors / serialization)

🧠 Key Rules (Must Memorize)

- Variables store references, not objects
- Assignment copies references
- Shallow copy copies the container
- Deep copy copies the entire object graph
- Immutable elements are safe with shallow copy
- Mutable nested objects require deep copy

🔥 Common Interview Traps

- b = a is NOT a copy
- copy() is shallow, not deep
- Shallow copy breaks with nested lists
- Java clone() is shallow and discouraged

🎯 One-Line Interview Answer

“Assignment duplicates references. A shallow copy duplicates the container but shares inner object references. A deep copy duplicates everything.”

🧩 Mental Model
```
Assignment      → same object
Shallow copy    → new container, same contents
Deep copy       → new container, new contents
```


## 📌 Python String Operations – Quick Notes

**Strings are immutable → every operation returns a new string**

“Python strings are immutable sequences that support indexing, slicing, and a rich set of built-in methods for transformation and searching.”

🔹 Basic Operations

- len(s) → number of characters
- Indexing → starts at 0
- Negative indexing → last character at -1

```python
s = "python"
s[0]    # 'p'
s[-1]   # 'n'
```

🔹 Case Conversion

- upper() → converts to uppercase
- lower() → converts to lowercase
- capitalize() → first letter uppercase, rest lowercase

```python
"hello".upper()       # "HELLO"
"HELLO".lower()       # "hello"
"python".capitalize() # "Python"
```

🔹 Whitespace Handling

- strip() → removes leading & trailing spaces
- lstrip() → removes left spaces
- rstrip() → removes right spaces

```python
"  hi  ".strip()  # "hi"
"---hi--i---".strip("-") # "hi--i
```

🔹 Splitting & Joining

- split() → splits string into a list

```python
"a,b,c".split(",")  # ['a', 'b', 'c']

list1 = ["this", "is", "string"]
s = "-".join(list1) # this-is-string
s = "hello\nbrajesh"
s = "hello\tbrajesh" # hello    brajesh
print(ord('a')) # 97 (ascii value - ord())
```

🔹 Replace & Modify

- replace(old, new) → replaces substring

🔹 Slicing (Very Important)
s[start : end : step]


Examples:
```
s = "programming"
s[0:7]     # "program"
s[:5]      # "progr"
s[::2]     # "pormig"
s[::-1]    # reverse string
```

🔹 Checking Prefix & Suffix

- startswith(prefix)
- endswith(suffix)

```
"hello.py".endswith(".py")  # True
```

🔹 Searching in String

- find(sub) → returns index or -1
- index(sub) → returns index or raises error
  
```
s = "coding"

s.find("d")   # 2
s.find("x")   # -1

s.index("d")  # 2
# s.index("x") → ValueError
```

🧠 Must-Remember Rules

- Strings are immutable
- Slicing creates a new string
- No in-place modification
- Negative indexing works everywhere



Set

- len(), add(), clear(), discard(), copy(), no indexing
- set Operations, union(), intersection(), difference(), symmetric_difference()


Dictionary

- len(), pop(), items(), get(), copy(), keys(), values(), update(), clear()
- get(key, default_value), setdefault(key, default)

🧠 Dictionary Key Rules

- Keys must be hashable
- Keys compared using ==
- If a == b and hash(a) == hash(b) → same key
- 1, 1.0, True → ❗ same key
- dict(key=value) → key is a string
- pop() requires the exact key

**“Python dictionary keys are compared by equality and hash value, so 1, 1.0, and True collide and overwrite each other.”**

