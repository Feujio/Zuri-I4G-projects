#!/usr/bin/env python3

from collections import Counter


def read_file_content(filename):
    """Read text from a file

    Args:
        filename (string): path to the file

    Returns:
        list: A list of strings
    """
    content = []

    with open(filename, 'r') as file:
        content = file.readlines()

    return content


def count_words():
    """count the occurence of words in that text

    Returns:
        Counter: A Counter object
    """
    text = read_file_content("./story.txt")
    result = Counter()

    for line in text:
        words = line.split()
        result = Counter(words)

    return result

count_words()
