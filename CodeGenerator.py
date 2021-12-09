from gibberish import Gibberish
import random
from numpy.random import shuffle


class CodeGenerator:
    def __init__(self, tab_spaces=4):
        self.TAB = tab_spaces * " "
        self.gib = Gibberish()

        random.seed(1)

    def create_var_name(self):
        return self.gib.generate_word() + str(random.randint(0, 10))

    def choose_rand_value(self):
        values = [
            random.randint(1, 100),
            self.gib.generate_words(random.randint(1, 5)),
            "'" + (" ".join(self.gib.generate_words(random.randint(1, 5)))) + "'",
            True,
            False
        ]
        shuffle(values)
        return values[0]

    def create_variable(self, equals=" = "):
        return self.create_var_name() + equals + str(self.choose_rand_value())

    def create_args_for_func(self, use_self=False):
        args = [
            f"{random.choice([self.create_var_name(), ''])}",
            f"{random.choice([self.create_variable(equals='='), ''])}",
            f"{random.choice(['*args', ''])}",
            f"{random.choice(['**kwargs', ''])}"
        ]

        output = ""

        if use_self:
            output += "self, "

        for idx, arg in enumerate(args):
            if arg != "":
                output += arg + ", "

        return output[:-2]

    def create_if_expression(self, executable=False):
        samples = [
            "True == True",
            "False == False",
            f"{random.randint(0, 10)} == {random.randint(0, 10)}",
            f"{self.choose_rand_value()} == {self.choose_rand_value()}",
            random.randint(-100, 200)
        ]

        expression = f"{executable} and ({random.choice(samples)} or True)"

        return expression

    def create_for_block(self, curr_positon="", _depth=1):
        curr_block_spaces = curr_positon + self.TAB
        block = [
            curr_positon + f"for {self.gib.generate_word() + str(random.randint(0, 10))} "
            f"in {range(random.randint(10,30))}:"
        ]
        for i in range(random.randint(1, 2)):
            block.append(curr_block_spaces + self.create_variable())

        block.append(self.create_body(curr_positon=(curr_positon + self.TAB), _except=["for"], _depth=_depth))

        return block

    def create_if_block(self, curr_positon="", _depth=1):
        block = [
            curr_positon + f"if {self.create_if_expression(executable=random.choice([True, False]))}:",
            self.create_body(curr_positon=(curr_positon + self.TAB), _except=["if"], _depth=_depth)
        ]

        return block

    def create_body(self, curr_positon="", _except=None, _depth=1):
        if _except is None:
            _except = []

        body = []

        if "var" not in _except:
            body.append(curr_positon + self.create_variable())

        if _depth > 0:
            _depth -= 1
            if "for" not in _except:
                body.append(self.create_for_block(curr_positon=curr_positon, _depth=_depth))
            if "if" not in _except:
                body.append(self.create_if_block(curr_positon=curr_positon, _depth=_depth))

        return body

    def create_class(self, curr_positon=""):
        inner_position = curr_positon + self.TAB
        return [
            curr_positon + f"class {self.create_var_name()}:",
            self.create_func(curr_positon=inner_position, use_self=True),
            self.create_func(curr_positon=inner_position, use_self=True),
        ]

    def create_func(self, curr_positon="", use_self=False):
        args = self.create_args_for_func(use_self=use_self)
        return [
            curr_positon + f"def {self.create_var_name()}({args}):",
            self.create_body(curr_positon=curr_positon + self.TAB, _depth=2),
            curr_positon + self.TAB + random.choice([f"return {self.choose_rand_value()}", "pass"])
        ]


if __name__ == "__main__":
    cg = CodeGenerator()
