# Object-Oriented Programming (Python)

Object-Oriented Programming (OOP) is a programming paradigm that employs objects—comprising both data (attributes) and behavior (methods)—to design and implement software. Here are the 4 main principles:

## 1. Encapsulation

Encapsulation binds data (attributes) and methods (that operate on this data) into a single unit or class, thus shielding the internal state of an object from direct modifications.

- **Attributes (variables)**: Symbolize an object's state.
- **Methods (functions)**: Denote actions an object can execute.

Encapsulation minimizes code complexity and maintains the object's internal state correctly.

## 2. Abstraction

Abstraction hides complex implementation details while only revealing the essential functionalities of an object. This ensures objects can be used without understanding their detailed workings.

- **Simplify the interface**: Showcase only essential details.
- **Reduce change's impact**: Thanks to abstraction, changes in a class's internal structure minimally affect other parts of the system utilizing the class.

## 3. Inheritance

Inheritance enables a new class to acquire attributes and behaviors (methods) from an existing class. This encourages code reuse and establishes a relationship between the base (parent) class and the derived (child) class.

- **Eliminate redundant code**: Instead of duplicating code in different classes, a class can inherit common attributes and methods from another.

## 4. Polymorphism

Polymorphism allows functions, methods, or objects to function in various ways. In Python, polymorphism is implicitly used due to its dynamic-typing nature.

- **Streamline method calls**: Rather than determining object types, the same method name can be used across various classes.

## Additional Key Terms:

- **class**: Outlines a blueprint for crafting objects (a specific data structure).
- **__init__()**: A special method in Python classes. This constructor is triggered when an object is instantiated.
- **self**: Represents the instance of the class and is utilized to access class attributes and methods.
- **super()**: A function used to invoke a method from the parent class.

## Exceptions in Python

Exceptions provide a means to handle potential errors during program execution. They enable the definition of custom errors, allowing the software to tackle exceptions and proceed with its operations. This ensures the application can elegantly manage unforeseen errors instead of ending suddenly.

```python
try:
    # Code that might produce an exception
except Exception as error:
    # Address the error
else:
    # Code to execute if no exception occurs
finally:
    # Run code after the try and except, irrespective of the result
