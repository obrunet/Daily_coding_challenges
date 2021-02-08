"""Anagram - https://exercism.io/tracks/python/exercises/anagram
An anagram is a rearrangement of letters to form a new word.
Given a word and a list of candidates, select the sublist of anagrams of the given word.
Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana"
the program should return a list containing "inlets"."""
 

def is_anagram(str_a, str_b):
    """Return True if both input strings are anagrams"""
    return sorted(str_a) == sorted(str_b)
 

def select_anagrams(st, lst):
    """Return the index of the input list 'lst' of elements / words that
    are anagrams of the input string 'st' """
    anagrams_idx = []
    for i, w in enumerate(lst):
        if is_anagram(st, w):
            anagrams_idx.append(i)
    return anagrams_idx
 

lst = ["enlists", "google", "inlets", "banana", "istenl"]
word = "listen"
result = select_anagrams(word, lst)
print(f"The anagrams' list of the word '{word}' is {[lst[idx] for idx in result]}")