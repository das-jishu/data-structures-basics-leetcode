"""
# LONGEST WORD IN DICTIONARY

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""

from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (len(x), x))
        trie = Trie()
        longestWord = (None, 0)
        for word in words:
            flag = trie.insert(word)
            if flag and len(word) > longestWord[1]:
                longestWord = (word, len(word))
                
        return longestWord[0] if longestWord[0] is not None else ""
        
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
        self.root[self.endSymbol] = True
        
    def insert(self, word):
        current = self.root
        flag = True
        for letter in word:
            if self.endSymbol not in current:
                flag = False
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = True
        return flag