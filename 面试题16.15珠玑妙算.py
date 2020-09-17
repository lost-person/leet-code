# coding = utf-8

from collections import Counter


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        a = sum(i == j for i, j in zip(solution, guess))
        b = sum((Counter(solution) & Counter(guess)).values())
        return [a, b - a]
