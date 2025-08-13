# Python Piscine 00 – Introduction to Python

## Description

This repository contains the **Python 00** project from the 42 School Data Science Piscine. It is the first module in the Python series, designed to introduce students to basic Python concepts and syntax. Each exercise aims to build a strong foundation through hands-on tasks, exploring data structures, types, control flow, functions, packaging, and more.

The exercises in this project are self-contained and progressively build your Python skills. Every folder from `ex00` to `ex09` has its own `README.md` explaining the objective, expected output, and constraints.

## Installation

> 🐍 Make sure you have **Python 3.10** installed on your system.

To set up your environment:
```bash
# Clone the repo
git clone https://github.com/tehuanmelo/python-piscine.git
cd python-00

# Optional: Create a virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install any required packages for ex09
pip install -r requirements.txt
```

## Usage

Each exercise is in its own directory, from `ex00/` to `ex09/`. To run an individual exercise:
```bash
cd ex0X/
python3 filename.py
```

For example:
```bash
cd ex04/
python3 whatis.py 42
```

Some exercises (like `ex05`, `ex06`, `ex07`) expect arguments to be passed through the command line. Others may require the use of a `tester.py` script provided.

## Project Structure

- [ex00/](./ex00) – First Python script
- [ex01/](./ex01) – Formatting time and date using packages
- [ex02/](./ex02) – Understanding object types with functions
- [ex03/](./ex03) – Detecting Python NULL types
- [ex04/](./ex04) – Checking if a number is even or odd via CLI
- [ex05/](./ex05) – Counting character types in a string
- [ex06/](./ex06) – Recreating `filter()` and applying string filters
- [ex07/](./ex07) – Encoding strings to Morse Code using dictionaries
- [ex08/](./ex08) – Reimplementing a loading bar (`tqdm`) using generators
- [ex09/](./ex09) – Creating and installing your first Python package

Each directory includes:
- `.py` files for implementation
- Proper error handling and `main()` structure
- `README.md` with explanations

## Configuration

The following are required or recommended:
- Python version: **3.10**

**Coding standards:**
- No global code — always functions.
- Use a `main()` entry point for scripts.
- Proper exception handling is required.
- All functions must have a `__doc__` string.
- No usage of `from module import *`.
- No global variables.

## License

This project is released under the MIT License as required in `ex09`.

## Author / Contact

**tde-melo**  
If you want to reach out you can find me on slack.

> By Odin, by Thor — use your brain and enjoy the ride!