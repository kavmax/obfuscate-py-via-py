from CodeInserter import CodeInserter

# Read file
file = open(f"./Examples/Inputs/anything.py", "r")
read_lines = file.readlines()

# Process
code_inserter = CodeInserter(file_lines=read_lines, iterations=1)
code_inserter.start()

# Output
code_inserter.console_print_lines()
