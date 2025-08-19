# Exercise 05 – First Standalone Program in Python

## Description

In this exercise, I created a standalone Python program that analyzes a given text and returns a summary of its content.  
The goal was to practice reading input from the command line or standard input, counting different types of characters, and displaying the results in a formatted output.

## Files and Structure

- **Directory:** `ex05/`
- **File to submit:** `building.py`
- **Allowed functions:** `sys` or any standard library to handle input

## What I Did

I wrote a script that:

1. Accepts one string argument from the terminal or prompts the user for input if no argument is provided.
2. Validates that only one argument is passed. If more are given, it raises:  
   `AssertionError: more than one argument is provided`
3. Parses the text and counts:
   - Total number of characters
   - Uppercase letters
   - Lowercase letters
   - Punctuation marks
   - Spaces
   - Digits
4. Prints a summary with all these statistics in a clear format.

## What I Learned

- How to read command-line arguments with `sys.argv`
- How to read from standard input using `sys.stdin.readline()`
- How to classify characters using string methods like `.isupper()`, `.islower()`, `.isspace()`, `.isdigit()`
- How to handle errors gracefully, including `EOFError`, `AssertionError`, and `KeyboardInterrupt`
- How to organize code using helper functions and keep logic clean and modular

## Example Output

### With an argument:

```
$> python building.py "Python 3.0, released in 2008!"
The text contains 29 characters:
1 upper letters
15 lower letters
3 punctuation marks
4 spaces
6 digits
$>
```

### Without an argument (interactive mode):

```
$> python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

### Invalid usage:

```
$> python building.py "Hello" "World"
AssertionError: more than one argument is provided
```

## How to Run

### ▶️ 1. With a command-line argument:

```bash
python building.py "This is a test message!"
```

### 📝 2. In interactive mode:

```bash
python building.py
```

Then type your message and press `Enter`. To simulate EOF, use `Ctrl+D` on Linux/macOS or `Ctrl+Z` then `Enter` on Windows.

## Challenges

- Handling input from both the command line and standard input
- Making sure all error cases (extra args, empty input, interruptions) were covered
- Designing the script so it's user-friendly and robust

## Final Thoughts

This was a great exercise to build a fully functional standalone CLI tool.  
It showed me how to handle user input, write structured code, and deliver a useful summary based on text processing.

> By Odin, by Thor! Use your brain!