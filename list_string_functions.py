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