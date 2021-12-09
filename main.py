from CodeInserter import CodeInserter

# Input files for testing
input_file_paths = [
    "anything.py",
    "password_generator.py",
    "pelicanconf.py",
    "pong_game/main.py",
    "atbash_cipher/atbash_cipher_test.py"
]
# Iterations for testing on each input file
iterations = [1, 2, 3, 5, 10]

for input_file_path in input_file_paths:
    for iteration_value in iterations:
        # Read file
        file = open(f"./Examples/Inputs/{input_file_path}", "r")
        read_lines = file.readlines()

        # Process
        code_inserter = CodeInserter(file_lines=read_lines, iterations=iteration_value)
        code_inserter.start()

        # Output
        code_inserter.save_to_file(
            f"./Examples/Outputs/{iteration_value}-iterations/{input_file_path}"
        )
        # code_inserter.console_print_lines()

