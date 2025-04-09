# Dynamic Attribute Assignment Class Pattern

## Overview
This Python class demonstrates a compact pattern for automatically assigning constructor arguments to instance attributes without explicit declaration.

## How It Works

### Traditional Approach
```python
class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
```

## Key Features
1. Automatic Attribute Assignment:

Dynamically assigns all constructor parameters as instance attributes

2. No manual self.x = x required for each parameter

## Implementation Details:

- Uses __init__.__code__.co_varnames to get parameter names

- Filters out self (first parameter)

- Updates self.__dict__ with {name:value} pairs

- Wrapped in lambda to create local scope

## Benefits
- Reduced Boilerplate: Eliminates repetitive assignment lines

- Maintainable: Automatically handles new parameters

- Consistent: Ensures uniform attribute creation

## Limitations
- Readability: More complex than explicit assignment

- Debugging: Harder to trace attribute assignments

- No Validation: No type checking or value validation

## When to Use
- When class has many simple attributes

- For rapid prototyping

- In internal/non-public APIs where readability is less critical

## Author
Pedro Trajano Ferreira
pedro.trajano.ferreira@gmail.com
04/09/25