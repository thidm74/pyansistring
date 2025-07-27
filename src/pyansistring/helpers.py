__all__ = [
    "find_spans",
    "search_separators",
    "rsearch_separators",
    "clamp",
    "hsl_to_rgb",
    "ValueRange",
    "Length",
]

from collections.abc import Generator
from dataclasses import dataclass

from pyansistring.constants import WHITESPACE


def find_spans(string: str, substring: str) -> Generator[tuple[int, int], None, None]:
    i = j = 0
    while i < len(string):
        i = string[i:].find(substring)
        if i == -1:
            break
        yield (i + j, i + j + len(substring))
        j = i = i + j + len(substring)


def search_separators(string: str, allowed: set[str] = WHITESPACE):
    """Search for allowed separators in a string."""
    separator = ""
    for char in string:
        if char in allowed:
            separator += char
        elif separator:
            yield separator
            separator = ""
    if separator:
        yield separator


def rsearch_separators(string: str, allowed: set[str] = WHITESPACE):
    """Search for allowed separators in a reversed string."""
    return search_separators(string[::-1], allowed)


def clamp(
    value: int | float,
    min_: int | float = float("-inf"),
    max_: int | float = float("inf"),
) -> int | float:
    """Restrict a number between two other numbers."""
    return min_ if value < min_ else max_ if value > max_ else value


def hsl_to_rgb(
    hue: int | float, saturation: int | float = 100, lightness: int | float = 50
) -> tuple[int, int, int]:
    hue = hue / 100
    saturation = saturation / 100
    lightness = lightness / 100

    def f(n: int | float):
        k = (n + hue * (10 / 3)) % 12
        a = saturation * min(lightness, 1 - lightness)
        return round((lightness - a * max(-1, min(k - 3, 9 - k, 1))) * 255)

    return f(0), f(8), f(4)


@dataclass(frozen=True)
class ValueRange:
    lo: int
    hi: int

    def __hash__(self) -> int:
        return hash((self.lo, self.hi))


@dataclass(frozen=True)
class Length:
    value: int

    def __hash__(self) -> int:
        return hash(self.value)
