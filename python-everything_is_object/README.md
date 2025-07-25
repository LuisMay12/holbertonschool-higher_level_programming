# Python Objects, Mutability, References & Aliasing

## Background Context

Now that we understand that everything is an object in Python, let's take a closer look at how Python works with different types of objects.

Have you ever modified a variable without knowing or wanting to? For example:

```python
a = 1
b = a
a = 2
print(b)  # Output: 1
```

But what about this?

```python
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # Output: ['x', 2, 3]
```

This project explores Python's behavior concerning objects, references, aliases, mutation, and assignment.

## Approach

This project differs from the usual:
- The first part is only questions about Python’s specifics (e.g., "What would be the result of…").
- **Read all documentation first, then think and brainstorm about your answers before coding.**
- Only test in the interpreter after careful consideration.
- Understand the reasoning behind the answers to apply the same logic to new problems.
- These types of questions frequently arise in Python interviews.

**All answers** must be only one line, with no extra spaces before or after.

## Resources

You are expected to read/watch:
- [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types (StackOverflow)](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation (Composing Programs, only this chapter)](https://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects)
- [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- Python tuples: immutable but potentially changing

## Learning Objectives

You should be able to explain, without Google:

- What is an object?
- Difference between a class and an object/instance
- Difference between immutable and mutable objects
- What is a reference?
- What is an assignment?
- What is an alias?
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (memory address in CPython)
- What is mutable and immutable?
- What are the built-in mutable types?
- What are the built-in immutable types?
- How does Python pass variables to functions?

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted with Python 3.8.5 on Ubuntu 20.04 LTS
- All files must end with a new line
- The first line must be exactly `#!/usr/bin/python3`
- The code must be executable and follow `pycodestyle` (2.7.*)
- File length will be checked with `wc`

### .txt Answer Files

- Only one line
- No Shebang at the top
- All files should end with a new line
