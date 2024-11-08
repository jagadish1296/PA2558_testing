import pytest
import sys
import os

#Adding the parent directory to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from list_string_functions import rotate_list   #Importing rotate_list from list_string_functions file

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]   #rotate right by 2
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]  #rotate left by 2
    assert rotate_list([], 3) == []                             #Edge case for empty list 