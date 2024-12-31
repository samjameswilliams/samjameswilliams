# Rust notes

*13/12/2024*

## tuples

Like Python tuples can contain multiple data types. You can also do multiple assignments on a single line like you can in Python. In Python this is generally called "tuple unpacking" whereas in Rust it's called "destructuring". 

Unlike Python, in Rust you can declare tuples as mutable and change values inside. You can get values by index with dot notation. `tuple.0` for the first value and so on. 

An empty tuple `()` is referred to as the "unit" tuple and is what you get instead of a `None` where there is no value from an expression.

## arrays

+ single data type.  
+ fixed length.  
+ enclosed in square brackets []  
+ stack allocated.  
+ access by index with square brackets `array[0]`

So a bit like numpy arrays but not just for numbers and not readily n-dimensional.

## functions and variables naming style

As in Python the naming style for functions and variables is `lower_snake_case`.

## functions

Unlike Python you don't need to define a function before you use it, you can define it after you first use it.

*16/12/2024*

## ownership

This is something I knew was going to be different but the Rust book does a very good job of introducing the concept. 

It's about pointers. If a variable `a` is allocated to the stack, then another variable is assigned `b = a`, Rust makes a copy of the variable in the stack. In this case there's no issue around ownership or pointers. If however `a` is heap allocated then instead of copying the data assigned to `a` when assigning `b = a`, Rust creates a new pointer to the same data so both `a` and `b` have pointers to the same data in memory.

In Python you get somewhat similar behaviour between immutable and mutable types as shown below:

```python
>>> # With an immutable type it's like making a copy
>>> a = 1
>>> b = a
>>> b += 1  # changing b doesn't change a
>>> print(f"a:{a}\nb:{b}")
a:1
b:2
>>> # But with mutable types it's different
>>> a = [1]
>>> b = a
>>> print(f"a:{a}\nb:{b}")
a:[1]
b:[1]
>>> # Changing b changes a
>>> b[0] = b[0] + 1
>>> print(f"a:{a}\nb:{b}")
a:[2]
b:[2]
>>> # And changing a changes b
>>> a[0] += 1
>>> print(f"a:{a}\nb:{b}")
a:[3]
b:[3]
```

The last step wouldn't work in Rust if the data was heap allocated because ownership can only reside with one variable at a time. The data would have "moved" to `b` in Rust so you wouldn't be able to change `a`.

However, it also wouldn't let you use `a` after "moving" the data to `b`, even just printing it. Rust behaves really differently to Python in this way. The ownership rules really force you to think about these things.

In the Python example above there's nothing stopping you doing something like

```python
>>> c, d, e, f, g, h = a, b, a, b, a, b
>>> j = [a, b, c, d, e, f, g, h]
>>> k = [i.append(i[-1]+1) for i in j]
>>> j
[[3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11],
 [3, 4, 5, 6, 7, 8, 9, 10, 11]]
```
where you can modify the list using any of 8 variable names (or as many as you want) all at the same time.

Rust's ownership rules wouldn't let you do this, at least, not without explicitly switching ownership, you wouldn't have more than one alias able to change the data at any one time.

The [Rust book](https://rust-book.cs.brown.edu/ch04-01-what-is-ownership.html) puts it like this:

> Moved heap data principle: if a variable x moves ownership of heap data to another variable y, then x cannot be used after the move.

So the Python shenanigans above would be prevented by the compiler which would tell you that the value had moved.

The summary at the end of the first section on ownership says

* All heap data must be owned by exactly one variable.  
* Rust deallocates heap data once its owner goes out of scope.  
* Ownership can be transferred by moves, which happen on assignments and function calls.  
* Heap data can only be accessed through its current owner, not a previous owner.  
