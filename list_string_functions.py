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

def find_longest_word(sentence):
    """
    Finds the longest word in a given sentence.
    
    :param sentence: The input sentence
    :return: The longest word in the sentence
    """
    words = sentence.split()
    return max(words, key=len) if words else ""


# This block will run when you execute the file directly
if __name__ == "__main__":
    # Test cases to see output when running the script directly
    print("Testing rotate_list:")
    print(rotate_list([1, 2, 3, 4, 5], 2))  # Should print [4, 5, 1, 2, 3]
    print(rotate_list([1, 2, 3, 4, 5], -2))  # Should print [3, 4, 5, 1, 2]
    print(rotate_list([], 3))  # Should print []

    print("\nTesting find_longest_word:")
    print(find_longest_word("The quick brown fox"))  # Should print "quick"
    print(find_longest_word("Python programming"))  # Should print "programming"
    print(find_longest_word(""))  # Should print an empty string ""
