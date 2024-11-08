# list_string_functions.py

def rotate_list(lst, k):
    """
    Rotates a list by k positions.
    
    :param lst: The input list
    :param k: Number of positions to rotate (positive for right rotation, negative for left)
    :return: The rotated list
    """
    if not lst:
        return []
    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]


# This block will run when you execute the file directly
if __name__ == "__main__":
    # Test cases to see output when running the script directly
    print("Testing rotate_list:")
    print(rotate_list([1, 2, 3, 4, 5], 2))  # Should print [4, 5, 1, 2, 3]
    print(rotate_list([1, 2, 3, 4, 5], -2))  # Should print [3, 4, 5, 1, 2]
    print(rotate_list([], 3))  # Should print []
