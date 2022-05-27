#!/usr/bin/env python3

def find_anagram(word, anagram):
    """Dtermine if two strings are anagrams

    Args:
        word (str): the subject
        anagram (str): a potential anagram

    Returns:
        bool: Trie if the two arguments are anagrams
    """
    for char in word:
        if char not in anagram:
            return False
        if word.count(char) != anagram.count(char):
            return False
    for char in anagram:
        if char not in word:
            return False
    return True

find_anagram("hello", "check")