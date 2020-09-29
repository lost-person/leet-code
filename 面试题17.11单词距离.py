# coding = utf-8
from typing import List

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        res = float("inf")
        if not words or len(words) < 2: return res

        i, n = 0, len(words)
        for j, word in enumerate(words):
            if word == word1 or word == word2:
                if words[i] != word and (words[i] == word1 or words[i] == word2):
                    res = min(res, j - i)
                i = j
        return res