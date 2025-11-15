import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Variables in Python

    In Python, variables are containers for storing data values. Unlike statically typed languages (e.g., Java or C++), Python is **dynamically typed**, meaning you don't need to declare the type of a variable upfront. The type is inferred from the value assigned to it and can even change during execution if you reassign a different type to the same variable name.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    For example:
    """)
    return


@app.cell
def _():
    x = 5  # x is an integer (int)
    x = "Hello"  # Now x is a string (str)
    return (x,)


@app.cell
def _(mo):
    mo.md(r"""
    To check the type of a variable, use the built-in `type()` function:
    """)
    return


@app.cell
def _(x):
    print(type(x))  # Output: <class 'str'>
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Common Types of Python Variables (Data Types)

    Python has several built-in data types that variables can hold. These are categorized into **immutable** (cannot be changed after creation) and **mutable** (can be modified). Below is a table summarizing the most common ones, with examples:

    | Data Type   | Category   | Description                                                                 | Example                          | Mutable? |
    |-------------|------------|-----------------------------------------------------------------------------|----------------------------------|----------|
    | `int`      | Number    | Whole numbers (no size limit in Python 3).                                  | `age = 25`                      | No      |
    | `float`    | Number    | Decimal numbers.                                                            | `height = 5.9`                  | No      |
    | `complex`  | Number    | Complex numbers (real + imaginary parts).                                   | `z = 3 + 4j`                    | No      |
    | `str`      | Text      | Immutable sequence of characters (strings). Supports single/double quotes.  | `name = "Alice"`                | No      |
    | `bool`     | Logic     | Boolean values: `True` or `False`.                                          | `is_valid = True`               | No      |
    | `list`     | Sequence  | Ordered, mutable collection of items (allows duplicates).                   | `fruits = ["apple", "banana"]`  | Yes     |
    | `tuple`    | Sequence  | Ordered, immutable collection of items (allows duplicates).                 | `coords = (10, 20)`             | No      |
    | `dict`     | Mapping   | Unordered (pre-Python 3.7), mutable key-value pairs (keys must be unique).  | `person = {"name": "Bob", "age": 30}` | Yes     |
    | `set`      | Set       | Unordered, mutable collection of unique items.                              | `unique_nums = {1, 2, 3}`       | Yes     |
    | `NoneType` | Special   | Represents the absence of a value (`None`).                                 | `result = None`                 | No      |

    #### Key Notes:
    - **Numbers**: `int` and `float` handle arithmetic operations seamlessly (e.g., `5 + 3.2` results in `8.2`, a float).
    - **Sequences** (`list`, `tuple`): Indexed (0-based), e.g., `fruits[0]` gives `"apple"`.
    - **Collections** (`dict`, `set`): No indexing by position; `dict` uses keys, `set` uses membership checks.
    - **Type Conversion**: Use functions like `int("5")`, `str(10)`, or `list("abc")` to convert between types.
    - **Advanced Types**: Python also supports user-defined types (classes), bytes (`bytes`), bytearrays, and more via libraries.

    For hands-on exploration, try running these in a Python interpreter or Jupyter notebook. If you meant something else (e.g., variable scopes like local/global), provide more details!
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Why `int` is Immutable in Python

    In Python, **mutability** refers to whether an object's internal state (its value or contents) can be modified *in place* after it's created. **Immutable** objects, like `int`, cannot be changed directly—any operation that appears to "modify" them actually creates a *new* object and rebinds the variable name to it. This is a deliberate design choice in Python, not a limitation.

    #### Reasons for Making `int` Immutable
    1. **Thread Safety**: Immutable objects are inherently safe to share across threads without locks or synchronization, as their value can't accidentally change.
    2. **Hashability and Caching**: Immutables can be hashed reliably (e.g., for use as dictionary keys or set elements). Python also caches small integers (-5 to 256) for efficiency, reusing the same object for the same value.
    3. **Simplicity and Predictability**: It prevents subtle bugs from side effects (e.g., one part of code changing a shared value unexpectedly) and makes code easier to reason about.
    4. **Performance Optimizations**: The interpreter can apply shortcuts, like interning strings or reusing integers, without worrying about mutations.

    In contrast, mutable types like `list` or `dict` allow in-place changes (e.g., `my_list.append(4)` modifies the existing list).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Demonstration
    Consider this code:
    """)
    return


@app.cell
def _():
    a = 5
    print(id(a))  # Memory address of the object

    a = a + 1  # This creates a NEW int object (6), doesn't modify 5
    print(id(a))  # Different memory address
    return


@app.cell
def _(mo):
    mo.md(r"""
    The `id()` function returns a unique identifier (essentially the memory address). The change in ID proves no mutation occurred—the original `5` remains unchanged forever. If you tried `a += 1` on a mutable object like a list, the ID would stay the same.

    This behavior applies to other immutable built-ins like `str`, `float`, `tuple`, and `bool`. If you need "mutable" numbers, use a wrapper like a list containing the value (e.g., `num = [5]; num[0] += 1`), but that's rarely necessary.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Lists in Python: A Mutable Data Type

    A **list** in Python is an ordered, flexible collection of items (which can be of mixed types) that can grow or shrink dynamically. It's one of the most commonly used mutable types, meaning you can change its contents *in place* without creating a new object. This contrasts with immutable types like `int` or `str`, where modifications create entirely new objects.

    #### Example: Demonstrating Mutability
    Here's a simple code example to show how lists are mutable:
    """)
    return


@app.cell
def _():
    # Create a list
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    print("Original ID:", id(fruits))  # Memory address of the list object

    # Modify in place: Append an item
    fruits.append("date")
    print("After append:", fruits)  # List now has 4 items
    print("ID after append:", id(fruits))  # Same ID—object wasn't recreated!

    # Modify in place: Change an element
    fruits[1] = "blueberry"
    print("After changing index 1:", fruits)  # "banana" replaced by "blueberry"
    print("ID after change:", id(fruits))  # Still the same ID

    # Modify in place: Remove an item
    fruits.remove("cherry")
    print("After remove:", fruits)  # List now has 3 items again
    print("ID after remove:", id(fruits))  # ID unchanged
    return


@app.cell
def _(mo):
    mo.md(r"""
    You can run this in a Python interpreter to see the IDs match—proving the *same object* is being modified.

    #### Why Are Lists Mutable?
    Python's designers (led by Guido van Rossum) made lists mutable for practical reasons tied to performance, flexibility, and real-world use cases:

    1. **Efficiency**: In-place changes (e.g., `append()` or `pop()`) are faster and use less memory than creating a new list each time. For large lists, this avoids unnecessary copying of data.

    2. **Dynamic Data Structures**: Lists are ideal for scenarios where data changes frequently, like:
       - Storing user inputs in a queue (e.g., a to-do list app).
       - Building results incrementally (e.g., collecting search hits in a web scraper).
       - Manipulating sequences in algorithms (e.g., sorting or filtering data).

    3. **Reference Semantics**: Python passes objects by reference, so mutability allows shared modifications. For example:
       ```python
       list1 = [1, 2]
       list2 = list1  # Both point to the same list object
       list2.append(3)
       print(list1)   # Output: [1, 2, 3] — change affects both!
       ```
       This is powerful for efficiency but requires care (use `copy.deepcopy()` if you need independent copies).

    4. **Trade-offs**: Mutability can introduce bugs (e.g., unintended side effects in functions), so Python provides immutable alternatives like `tuple` for cases where constancy is key (e.g., fixed coordinates).

    #### Quick Comparison: Mutable vs. Immutable Sequences
    | Type    | Mutable? | Example Operation                  | Creates New Object? | Use Case                  |
    |---------|----------|------------------------------------|---------------------|---------------------------|
    | `list` | Yes     | `my_list.append(4)`               | No                 | Dynamic collections      |
    | `tuple`| No      | `my_tuple = (1, 2) + (3,)`        | Yes                | Fixed data (e.g., records)|
    """)
    return


if __name__ == "__main__":
    app.run()
