# Exercise 04 – The Even and the Odd

## Description

In this exercise, I developed a command-line Python script to determine whether a given number is even or odd.  
The script validates the input and responds with a message or raises an appropriate error when the input is invalid.

## Files and Structure

- **Directory:** `ex04/`
- **File to submit:** `whatis.py`
- **Allowed functions:** `sys` or any other library that handles command-line arguments

## What I Did

I wrote a script that uses `sys.argv` to read the user input from the terminal. The program handles several cases:

- If no argument is provided, the program does nothing.
- If more than one argument is passed, it raises:  
  `AssertionError: more than one argument is provided`
- If the input is not an integer, it raises:  
  `AssertionError: argument is not an integer`
- If the input is a valid integer:
  - It prints `"I'm Even."` if the number is divisible by 2.
  - It prints `"I'm Odd."` if the number is not divisible by 2.

## What I Learned

- How to handle command-line arguments using `sys.argv`
- How to use `try`, `except`, and `assert` for input validation
- How to convert strings to integers safely
- The importance of user-friendly error messages in scripts

## Example Output

```
$> python whatis.py 14
I'm Even.
$>

$> python whatis.py -5
I'm Odd.
$>

$> python whatis.py
$>

$> python whatis.py 0
I'm Even.
$>

$> python whatis.py Hi!
AssertionError: argument is not an integer
$>

$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

## How to Run

Run the script from the terminal with a single number as an argument:

```bash
python whatis.py 7
```

Test it with different inputs to see how it behaves:

```bash
python whatis.py
python whatis.py abc
python whatis.py 10 20
```

## Challenges

- Handling multiple input errors without crashing
- Making sure empty input doesn't raise an exception
- Being strict with input types while keeping the code simple

## Final Thoughts

This was a simple but effective exercise to practice argument handling, type validation, and branching logic.  
It taught me how to write defensive code that guides users with meaningful error messages.

> By Odin, by Thor! Use your brain!