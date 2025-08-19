# Exercise 01 – First Use of a Package

## Description

In this exercise, I explored how to use Python’s built-in packages to work with time and date information.  
The goal was to write a script that prints the number of seconds since January 1, 1970 (Unix epoch), both as a float and in scientific notation, followed by the current date in a specific format.

## Files and Structure

- **Directory:** `ex01/`
- **File to submit:** `format_ft_time.py`
- **Allowed functions:** `time`, `datetime`, or any other time-related standard library

## What I Did

I created a script that retrieved the current timestamp and printed:

1. The number of seconds since January 1, 1970 as a float with four decimal places.
2. The same number in scientific notation (e.g., `1.67e+09`).
3. The current date in the format: `Mon DD YYYY` (e.g., `Oct 21 2022`).

I used the `time.time()` function to get the timestamp and formatted the output using string formatting techniques.

## What I Learned

- How to import and use standard Python libraries like `time` and `datetime`
- How to format float numbers with precision and scientific notation
- How to display dates in a human-readable format
- How to build terminal scripts that print well-formatted information

## Example Output

```
$> python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,755,109,238.0586 or 1.76e+09 in scientific notation
Aug 13 2025$
$>
```

## Challenges

- Formatting the timestamp with the correct number of decimal places
- Ensuring the scientific notation matched the expected format
- Handling localization differences in date formatting

## Final Thoughts

This exercise gave me hands-on practice with built-in time-related Python modules and improved my understanding of output formatting.  
It was a great step forward in building scripts that interact with real-world data and time-based logic.

> By Odin, by Thor! Use your brain!