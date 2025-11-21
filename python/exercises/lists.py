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
    # Python Lists
    [Churu Churu Website](https://www.churuchuru.com) | [Churu Churu Github Repo](https://github.com/churuchuru/churuchuru)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Python lists are one of the most versatile and commonly used data structures. They are **mutable**, ordered collections that can hold items of any type (including mixed types like integers, strings, or even other lists). Lists are defined using square brackets `[]` and support a wide range of operations for manipulation. This tutorial covers everything from basics to advanced features like list comprehensions, with examples you can run in a Python interpreter.

    ## 1. Basics of Lists
    ### Creating Lists
    - Empty list: `my_list = []`
    - With elements: `numbers = [1, 2, 3, 4]`
    - Mixed types: `mixed = [1, "apple", True, 3.14]`
    - From other iterables: Use `list()` function, e.g., `chars = list("hello")` → `['h', 'e', 'l', 'l', 'o']`
    - Nested lists: `matrix = [[1, 2], [3, 4]]` (lists within lists, useful for 2D arrays)

    Lists are zero-indexed, meaning the first element is at index 0: `numbers[0]` → `1`.

    ### Accessing Elements
    - By index: `numbers[2]` → `3`
    - Negative indexing: From the end, e.g., `numbers[-1]` → `4` (last element)
    - Out-of-range access raises `IndexError`, so check length with `len(numbers)` → `4`

    ## 2. Mutability and Basic Operations
    As discussed earlier, lists are mutable—you can change them in place without creating a new object.

    ### Adding Elements
    - `append(item)`: Adds to the end (efficient, O(1) time).
      ```python
      fruits = ["apple", "banana"]
      fruits.append("cherry")
      print(fruits)  # ['apple', 'banana', 'cherry']
      ```
    - `insert(index, item)`: Adds at a specific position (shifts elements, O(n) time).
      ```python
      fruits.insert(1, "blueberry")
      print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']
      ```
    - `extend(iterable)`: Adds multiple elements from another iterable (like another list).
      ```python
      fruits.extend(["date", "elderberry"])
      print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
      ```

    ### Removing Elements
    - `remove(item)`: Removes the first occurrence (raises `ValueError` if not found).
      ```python
      fruits.remove("banana")
      print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']
      ```
    - `pop(index=-1)`: Removes and returns the item at the index (default: last).
      ```python
      last = fruits.pop()
      print(last)    # 'elderberry'
      print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']
      ```
    - `clear()`: Empties the list.
      ```python
      fruits.clear()
      print(fruits)  # []
      ```
    - `del`: Deletes by index or slices (more on slices below).
      ```python
      del numbers[1]  # Removes index 1 (2)
      ```

    ### Other Common Methods
    Here's a table of essential list methods:

    | Method          | Description                                      | Example Input/Output                     | Returns |
    |-----------------|--------------------------------------------------|------------------------------------------|---------|
    | `append(x)`    | Add x to end                                     | `[1,2].append(3)` → `[1,2,3]`           | None   |
    | `extend(iter)` | Add elements from iter                           | `[1,2].extend([3,4])` → `[1,2,3,4]`     | None   |
    | `insert(i, x)` | Insert x at index i                              | `[1,3].insert(1,2)` → `[1,2,3]`         | None   |
    | `remove(x)`    | Remove first x                                   | `[1,2,2].remove(2)` → `[1,2]`           | None   |
    | `pop(i=-1)`    | Remove/return item at i                          | `[1,2,3].pop()` → 3; list: `[1,2]`      | Item   |
    | `clear()`      | Empty the list                                   | `[1,2].clear()` → `[]`                  | None   |
    | `index(x)`     | Index of first x (raises ValueError if absent)   | `[1,2,3].index(2)` → 1                  | int    |
    | `count(x)`     | Number of occurrences of x                       | `[1,2,2].count(2)` → 2                  | int    |
    | `sort(key=None, reverse=False)` | Sort in place (stable)                  | `[3,1,2].sort()` → `[1,2,3]`            | None   |
    | `reverse()`    | Reverse in place                                 | `[1,2,3].reverse()` → `[3,2,1]`         | None   |
    | `copy()`       | Shallow copy                                     | `a=[1,2]; b=a.copy();` b independent    | list   |

    - Sorting example: `numbers.sort()` sorts ascending; use `key=lambda x: abs(x)` for custom sorting.
    - For a sorted copy without mutating: Use `sorted(numbers)` (returns new list).

    ## 3. Slicing Lists
    Slicing creates a new list from a subset using `[start:stop:step]` (start inclusive, stop exclusive).
    - Basic: `numbers[1:3]` → `[2, 3]`
    - Omit start/stop: `numbers[:2]` → `[1, 2]`; `numbers[2:]` → `[3, 4]`
    - Step: `numbers[::2]` → `[1, 3]` (every second); `numbers[::-1]` → `[4, 3, 2, 1]` (reverse)
    - Assignment: `numbers[1:3] = [10, 20]` → `[1, 10, 20, 4]` (mutates in place)

    Slicing is efficient for copying: `copy_list = original[:]` (shallow copy).

    ## 4. List Comprehensions
    List comprehensions provide a concise way to create lists from iterables, often replacing loops. Syntax: `[expression for item in iterable if condition]`

    ### Basic Examples
    - Squares: `[x**2 for x in range(5)]` → `[0, 1, 4, 9, 16]`
    - Filtered: `[x for x in range(10) if x % 2 == 0]` → `[0, 2, 4, 6, 8]` (evens)
    - With transformation: `["even" if x % 2 == 0 else "odd" for x in range(5)]` → `['even', 'odd', 'even', 'odd', 'even']`

    ### Nested Comprehensions
    For flattening nested lists: `[item for sublist in matrix for item in sublist]` → `[1, 2, 3, 4]`

    ### Advanced: With Multiple Iterables
    `[(x, y) for x in [1,2] for y in ['a','b']]` → `[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]`

    Comprehensions are faster and more readable than equivalent `for` loops with `append()`. Use them for simple transformations; fall back to loops for complex logic.

    ## 5. Operators and Iteration
    - Concatenation: `[1,2] + [3,4]` → `[1,2,3,4]` (new list)
    - Repetition: `[0] * 3` → `[0,0,0]`
    - Membership: `"apple" in fruits` → `True`/`False`
    - Iteration: Use `for item in my_list:` or with indices: `for i, item in enumerate(my_list):`
    - Comparison: Lists compare lexicographically: `[1,2] < [1,3]` → `True`

    ## 6. Common Pitfalls and Best Practices
    - **Mutable Defaults in Functions**: Avoid `def func(lst=[]):`—the default is shared! Use `def func(lst=None): if lst is None: lst = []`
    - **Shallow vs. Deep Copies**: `copy()` or `[:]` copies the list but not nested objects. Use `copy.deepcopy()` from `import copy` for deep copies.
    - **Aliases**: `b = a` makes b reference the same list—changes to one affect both. Use `copy()` to avoid.
    - **Performance**: Lists are arrays under the hood; append/pop from end is fast, but insert/remove from start is O(n)—use `collections.deque` for queues.
    - **Type Hints**: In modern Python, use `from typing import List`; `def process(items: List[int]) -> List[int]:`
    - **Alternatives**: For unique items, use `set`; for immutable, `tuple`; for key-value, `dict`.

    ## 7. Advanced Topics
    - **Sorting with Keys**: `sorted(fruits, key=len)` → sorts by length.
    - **Zipping**: `list(zip([1,2], ['a','b']))` → `[(1, 'a'), (2, 'b')]`
    - **Functional Tools**: Use `map()`, `filter()`, e.g., `list(map(str, numbers))` → `['1', '2', '3', '4']`; but comprehensions are preferred.
    - **Memory Usage**: Large lists? Consider generators: `(x**2 for x in range(5))` (lazy, memory-efficient).
    - **Multidimensional**: For matrices, use nested lists or NumPy for efficiency.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 8. List Example with Marimo UI
    """)
    return


@app.cell
def _(mo):
    # Initialize state for tasks: a list of dicts with 'text' and 'done'
    tasks, set_tasks = mo.state([])


    # Function to add a new task
    def add_task(new_text):
        if new_text.strip():  # Avoid empty tasks
            new_tasks = tasks() + [{"text": new_text.strip(), "done": False}]
            set_tasks(new_tasks)
        return new_text  # Clear input after add


    # UI for adding tasks
    add_input = mo.ui.text(placeholder="Enter a new task...", label="Add Task")
    add_button = mo.ui.button(
        label="Add", on_click=lambda e: add_task(add_input.value)
    )
    add_row = mo.hstack([add_input, add_button])
    return add_row, set_tasks, tasks


@app.cell
def _(set_tasks, tasks):
    # Function to toggle done status
    def toggle_done(index):
        new_tasks = tasks()
        new_tasks[index]["done"] = not new_tasks[index]["done"]
        set_tasks(new_tasks)
    return (toggle_done,)


@app.cell
def _(mo, tasks, toggle_done):
    # Display the task list dynamically
    task_list = mo.vstack(
        [
            mo.hstack(
                [
                    mo.ui.checkbox(
                        value=task["done"],
                        on_change=lambda e, i=i: toggle_done(i),  # Capture index
                    ),
                    mo.md(task["text"]).style(
                        {
                            "text-decoration": "line-through"
                            if task["done"]
                            else "none"
                        }
                    ),
                ]
            )
            for i, task in enumerate(tasks())
        ]
    )
    return (task_list,)


@app.cell
def _(add_row, mo, task_list, tasks):
    # Main app layout
    mo.vstack(
        [
            mo.md("## 9. To-Do List"),
            add_row,
            mo.md(f"**Tasks ({len(tasks())}):**"),
            task_list if tasks() else mo.md("No tasks yet."),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
