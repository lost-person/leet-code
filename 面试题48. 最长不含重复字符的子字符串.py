# coding = utf-8


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        if n == 1:
            return n

        # res, low = 0, 0
        # for high in range(n):
        #     if s[high] not in s[low:high]:
        #         res = max(res, high - low + 1)
        #     else:
        #         while s[high] in s[low:high]:
        #             low += 1
        # return res

        char_dict = dict()
        tail = 0
        res = 0
        for high in range(n):
            if s[high] in char_dict:
                tail = max(char_dict[s[high]] + 1, tail)
            char_dict[s[i]] = high
            res = max(res, high - tail + 1)

        return res
