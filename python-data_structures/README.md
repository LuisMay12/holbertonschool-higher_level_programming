# Python Data Structures

## 3.1.3. Lists
Lists are one of the most versatile data structures in Python. They are ordered, mutable, and can contain elements of different types.

### Key Features:
- **Ordered**: Elements have a defined order.
- **Mutable**: You can modify the list after creation.
- **Dynamic**: Lists can grow or shrink as needed.

### Example:
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying elements
fruits[1] = "blueberry"

# Adding elements
fruits.append("orange")

# Removing elements
fruits.remove("cherry")
```

---

## Data Structures (up to 5.3. Tuples and Sequences)

### 5.1. More on Lists
Lists can be manipulated in various ways, such as slicing, sorting, and using list comprehensions.

#### Example:
```python
# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]

# Sorting
numbers.sort(reverse=True)
print(numbers)  # Output: [5, 4, 3, 2, 1, 0]

# List comprehension
squared = [x**2 for x in numbers]
print(squared)  # Output: [25, 16, 9, 4, 1, 0]
```

### 5.2. The del Statement
The `del` statement is used to delete elements or entire lists.

#### Example:
```python
# Deleting an element
del numbers[2]

# Deleting the entire list
del numbers
```

### 5.3. Tuples and Sequences
Tuples are immutable sequences, often used to group related data. Unlike lists, tuples cannot be modified after creation.

#### Example:
```python
# Creating a tuple
coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Output: 10

# Tuples are immutable
# coordinates[0] = 15  # This will raise an error
```

---

## Learn to Program 6: Lists
This section focuses on practical applications of lists, such as using them to store and manipulate data in real-world scenarios.

### Example:
```python
# Using lists to store user input
user_data = []
for _ in range(3):
    name = input("Enter a name: ")
    user_data.append(name)

print("Collected names:", user_data)
```

Lists are a fundamental part of Python programming, and mastering them is essential for working with data effectively.  