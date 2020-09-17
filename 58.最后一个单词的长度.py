#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0

        cnt, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            cnt += 1
            tail -= 1
        return cnt


# @lc code=end
