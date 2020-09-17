# coding = utf-8


class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "

        n = len(s)
        if n == 1:
            return s

        char_dict = {}
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1

        for c in s:
            if char_dict[c] == 1:
                return c
        return " "
