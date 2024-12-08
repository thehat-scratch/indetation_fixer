# indentation_fixer

## Overview

`indentation_fixer` is a Python package that allows developers to easily handle unindented or poorly indented code. It provides a decorator and helper function to process and execute Python code dynamically, even if it's written without proper indentation.

## Features

- Normalize and execute unindented Python code provided as strings
- Use a decorator to execute unindented code returned by functions
- Simplify workflows for quick prototyping and experimentation

## Installation

You can install `indentation_fixer` using pip:

```bash
pip install indentation_fixer
```
```bash
git clone https://github.com/thehat-scratch/indetation_fixer.git
cd indentation_fixer
pip install .
```
##Example of Usage

The following code demonstrates how to use the `allow_unindented` decorator to handle unindented code within a function:

```python
from indentation_fixer import allow_unindented

@allow_unindented
def my_code():
    return """
a = 5
b = 10
print(a + b)  # Outputs: 15
"""

my_code()

### Python Code Example: Execute Unindented Code

The following code demonstrates how to use the `execute_unindented_code` function to execute unindented Python code:

```python
from indentation_fixer import execute_unindented_code

code = """
x = 3
y = 7
print(x * y)  # Outputs: 21
"""

execute_unindented_code(code)


