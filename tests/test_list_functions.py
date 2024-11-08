def test_rotate_list():
    # Basic test cases for rotating the list
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]  # Rotate right by 2
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]  # Rotate left by 2
    assert rotate_list([], 3) == []  # Edge case for empty list
