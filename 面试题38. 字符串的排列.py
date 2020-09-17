# coding = utf-8

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        if not s:
            return res

        if len(s) == 1:
            res.append(s)
            return res

        s = ''.join(sorted(s))
        n = len(s)

        def backtrack(s: str, tmp: List[str]):
            if not s:
                res.append(''.join(tmp))
                return

            for i in range(len(s)):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                backtrack(s[:i] + s[i + 1:], tmp + [s[i]])

        backtrack(s, [])
        return res