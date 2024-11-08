# tests/test_list_functions.py

import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from list_string_functions import rotate_list  # Import rotate_list from list_string_functions

def test_rotate_list():
    # Basic test cases for rotating the list
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]  # Rotate right by 2
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]  # Rotate left by 2
    assert rotate_list([], 3) == []  # Edge case for empty list
