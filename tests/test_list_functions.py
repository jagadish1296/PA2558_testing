# tests/test_list_functions.py

import pytest
import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from list_string_functions import rotate_list, find_longest_word

def test_rotate_list():
    # Basic test cases for rotating the list
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotate_list([], 3) == []  # Edge case for empty list

def test_find_longest_word():
    # Basic tests for finding the longest word
    assert find_longest_word("The quick brown fox") == "quick"
    assert find_longest_word("Python programming") == "programming"
    assert find_longest_word("") == ""  # Edge case for empty string

def test_integration():
    # Integration test that combines the two functions
    sentence = "Rotate and find longest word in this sentence"
    rotated_list = rotate_list(sentence.split(), 3)  # Split sentence into a list and rotate it
    longest_word = find_longest_word(" ".join(rotated_list))  # Find the longest word in the rotated list
    assert longest_word == "sentence"  # After rotation, "sentence" should be the longest word
