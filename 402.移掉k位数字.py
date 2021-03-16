#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            stack.append(n)
        
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') or "0"
# @lc code=end

