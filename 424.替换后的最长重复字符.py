#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0

        n = len(s)
        if n == 1: return 1

        if n <= k: return n

        left, right = 0, 0
        max_freq = 0
        char_dict = dict()
        while right < n:
            c = s[right]
            char_dict[c] = char_dict.get(c, 0) + 1

            max_freq = max(max_freq, char_dict[c])
            if right - left + 1 > max_freq + k:
                char_dict[s[left]] -= 1
                left += 1
            right += 1

        return n - left


# @lc code=end
