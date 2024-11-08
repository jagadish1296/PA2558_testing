# tests/test_list_functions.py

import pytest
from list_string_functions import rotate_list, find_longest_word

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotate_list([], 3) == []

def test_find_longest_word():
    assert find_longest_word("The quick brown fox") == "quick"
    assert find_longest_word("Python programming") == "programming"
    assert find_longest_word("") == ""
