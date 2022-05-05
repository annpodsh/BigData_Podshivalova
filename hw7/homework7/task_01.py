"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool

>>> tree = {"first": ["RED", "BLUE"], "second": {"simple_key": ["simple", "of", "RED", "valued"]}}
>>> print(find_occurrences(tree, "RED"))
2
"""
from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    return str(tree.values()).count(str(element))


if __name__ == '__main__':
    import doctest
    print(find_occurrences(example_tree, "RED"))  # 6
