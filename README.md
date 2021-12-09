# ObfuscatePyViaPy
> Python obfuscator for Python files

This simple code takes .py source file and makes .py obfuscated via adding fake data to your code.

## Available fake data
It can generate fake:
- functions,
- classes,
- loops,
- if-blocks,
- variables;

## Usage
```Python3
from CodeInserter import CodeInserter

# Read file
file = open("input-filename.py", "r")
read_lines = file.readlines()

# Process
code_inserter = CodeInserter(file_lines=read_lines, iterations=2)
code_inserter.start()

# Output
code_inserter.save_to_file("output-filename.py")
```

`iterations` value shows the number of times your code has been processed
