import os
import builtins
import keyword

print(keyword.kwlist)


def ohms_law(v=0, i=0, r=0):
    if v == 0:
        result = i * r
        return result
    elif i == 0:
        result = v / r
        return result
    elif r == 0:
        result = v / i
        return result
    else:
        return 0


def open_file(path):
    f = builtins.open(path, 'r')
    return UpperCaser(f)


class UpperCaser:
    """
    Wrapper around a file that converts output to upper-case.
    """
    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()


# This is my comment
class Car:
    def __init__(self, name):
        self.name = name
        print(f"The car {self.name} has been created!")


my_car = Car("BMW")
print(
    my_car.name
)


cat = "B" \
      "A" \
      "R" \
      "SIK"


def read_book(book):
    for idx, page in enumerate(book):
        print(f"Page {idx+1}")
        for line in page:
            print(f"\t{line}")


read_book([
    ["Line 1", "Line 2", "Line 3"],
    ["Line 1", "Line 2", "Line 3"]
])

if __name__ == "__main__":
    print("__name__ guard works")
else:
    print("__name__ guard does not work")


try:
    x = 5 / 0
except ZeroDivisionError:
    print("Oops! You are trying to do something awful!")
finally:
    print("Goodbye, world!")
