"""The Word You'd Delete From the Dictionary — a make.fun entry.

Prints exactly one word and nothing else: the one word I would
erase from the dictionary forever.
"""

LINE = "Moist."


def build_line() -> str:
    line = LINE
    assert len(line.split()) == 1, "must be exactly one word"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
