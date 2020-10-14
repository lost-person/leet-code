#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_freq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])

        res = []
        for i in range(26):
            res.extend([chr(i + ord("a"))] * min_freq[i])
        return res
# @lc code=end

