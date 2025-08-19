# Exercise 02 – First Python Function

## Description

In this exercise, I practiced writing a custom function to detect and print the type of different Python objects.  
The objective was to build a function that prints the type of a given object in a formatted way and always returns the integer `42`.

## Files and Structure

- **Directory:** `ex02/`
- **File to submit:** `find_ft_type.py`
- **Allowed functions:** None

## What I Did

I wrote a function called `all_thing_is_obj` that receives any object as a parameter and checks its type using `type()`.  
Based on the type, the function prints a specific message:

- If the object is a list, tuple, set, or dictionary, it prints the type with a label.
- If the object is a string, it prints the string followed by a fun message and the type.
- If the type is not recognized, it prints `"Type not found"`.

Finally, the function always returns `42`, as required.

## What I Learned

- How to define functions with type hints in Python
- How to check object types using `type()` and compare with built-in types
- How to use conditional statements (`if`, `elif`, `else`)
- How to format strings using f-strings
- That `print()` output can be customized to reflect different object types

## Example Output

```
$> python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

## How to Run

You can run the exercise in two ways:

### ▶️ 1. Run manually using the `main()` function

```bash
python tester.py
```

This will call `all_thing_is_obj()` with sample values and print the output directly.

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

- Remembering to return `42` no matter the object
- Matching the format of the printed messages exactly as expected
- Understanding how `type()` and `is` comparisons work in Python

## Final Thoughts

This task helped reinforce how Python treats everything as an object.  
It was a fun and simple way to apply conditional logic and type introspection early in the Piscine.

> By Odin, by Thor! Use your brain!