# Exercise 03 – NULL Not Found

## Description

In this exercise, I implemented a function to identify and classify different representations of "null-like" values in Python.  
The objective was to print the type of the provided object if it matches one of the expected "null" types (e.g., `None`, `NaN`, empty string, `0`, or `False`) and return a code indicating success or failure.

## Files and Structure

- **Directory:** `ex03/`
- **File to submit:** `NULL_not_found.py`
- **Allowed functions:** None (except `math.isnan()`)

## What I Did

I wrote a function called `NULL_not_found()` that accepts a single parameter and:

- Detects if the object is:
  - `None`
  - A float `NaN`
  - The integer `0`
  - An empty string (`""`)
  - The boolean `False`
- Prints a custom message for each detected type along with its class
- Returns `0` if a known type was found, or `1` if the type was not recognized

Each known value was associated with a playful label like "Cheese" for `NaN` or "Fake" for `False`.

## What I Learned

- How to detect `None` and compare object types using `type()`
- How to check for `NaN` values using `math.isnan()`
- The difference between truthy and falsy values in Python
- How to use type-checking and conditionals together for clean control flow

## Example Output

```
$> python tester.py | cat -e
None : <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

## How to Run

You can run the exercise in two ways:

### ▶️ 1. Run manually using the `main()` function

```bash
python tester.py
```

This will call `NULL_not_found()` with sample values and print the output directly.

### 🧪 2. Run as automated tests using `pytest`

Make sure `pytest` is installed:

```bash
pip install pytest
```

Then run:

```bash
pytest -v tester.py
```

The `-v` flag is used to show a more discriptive information of the tests.

## Challenges

- Handling `NaN` comparison, since `NaN != NaN`
- Ensuring exact format of printed messages
- Being careful not to confuse empty strings, `0`, and `False`, even though all are falsy

## Final Thoughts

This was a clever exercise to explore the subtle differences between Python’s "empty" or "null" values.  
It helped me understand how Python distinguishes between various object types and how to manage them properly in code.

> By Odin, by Thor! Use your brain!