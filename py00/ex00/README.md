# Exercise 00 – First Python Script

## Description

In this exercise, I was introduced to basic Python data structures and how to manipulate and print their content.  
The goal was to update a list, tuple, set, and dictionary so that each one would display a custom greeting related to my campus.

## Files and Structure

- **Directory:** `ex00/`
- **File to submit:** `Hello.py`
- **Allowed functions:** None

## What I Did

I was given four predefined variables — a list, a tuple, a set, and a dictionary — each containing the word `"Hello"` followed by a second item with a placeholder value.  
My task was to change those placeholder values to display:

- `"World!"` in the list
- `"UAE!"` in the tuple
- `"Abu Dhabi!"` in the set
- `"42AbuDhabi!"` in the dictionary

I made sure that each structure had the exact values required and printed them in the correct format.

## What I Learned

- How to modify basic data structures in Python (`list`, `tuple`, `set`, `dict`)
- How to print them with correct formatting
- The importance of following output specifications precisely
- That sets are unordered, so their printed order may vary

## Example Output

```
$> python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'UAE!')$
{'Hello', 'Abu Dhabi!'}$
{'Hello': '42AbuDhabi!'}$
$>
```

## Challenges

- Ensuring the output matched the exact format, especially with line endings and spacing
- Remembering that tuples are immutable, so I had to recreate the tuple with new values instead of modifying it directly, and sets are unordered

## Final Thoughts

This was a simple but important exercise to get comfortable with Python’s basic types and syntax.  
It set the foundation for more complex tasks later in the Piscine.

> By Odin, by Thor! Use your brain!