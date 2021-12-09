from CodeGenerator import CodeGenerator
import copy
import os
import errno


class CodeInserter(CodeGenerator):
    def __init__(self, file_lines, iterations=1, tab_spaces=4):
        super().__init__(tab_spaces=tab_spaces)
        self.lines = file_lines
        self.iterations = iterations

    def start(self):
        self.prepare_lines()

        for i in range(self.iterations):
            self.insert_once()
            self.normalize_lines()

    def prepare_lines(self):
        for idx, line in enumerate(self.lines):
            if idx + 1 == len(self.lines):
                self.lines[idx] = line
            else:
                self.lines[idx] = line[:-1]

    def insert_once(self):
        new_lines = []

        for idx, line in enumerate(self.lines):
            line_is_not_empty = bool(line) and line[0] != "#"

            if line_is_not_empty:
                extra_spaces = " " * (len(line) - len(line.lstrip()))
                curr_ln = line.lstrip()

                # Inserts before current line
                if curr_ln.startswith("print") or \
                        curr_ln.startswith("if ") or \
                        curr_ln.startswith("try:"):
                    new_lines.append(self.create_for_block(curr_positon=extra_spaces))

                if curr_ln.startswith("class"):
                    new_lines.append(self.create_class(curr_positon=extra_spaces))

                # Class method without @modifier OR simple function
                if curr_ln.startswith("def") and not new_lines[-1].lstrip().startswith("@"):
                    new_lines.append(self.create_func(curr_positon=extra_spaces, use_self=True))

                # @modifier for class method
                if curr_ln.startswith("@"):
                    new_lines.append(self.create_func(curr_positon=extra_spaces, use_self=True))

                # Current line
                new_lines.append(line)

        self.lines = new_lines

    def list_deep_parser(self, line):
        tmp_list = []
        if type(line) is list:
            for _line in line:
                if type(_line) is list:
                    tmp_list.extend(self.list_deep_parser(_line))
                else:
                    tmp_list.append(_line)
            return tmp_list
        else:
            return line

    def normalize_lines(self):
        tmp_lines = copy.deepcopy(self.lines)
        self.lines = []

        for line in tmp_lines:
            new_line = self.list_deep_parser(line)
            if type(new_line) is list:
                self.lines.extend(new_line)
            else:
                self.lines.append(new_line)

    def console_print_lines(self):

        for idx, line in enumerate(self.lines):
            print(idx, line, sep="\t")

    def save_to_file(self, filename):
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as f:
            for line in self.lines:
                f.write("%s\n" % line)
