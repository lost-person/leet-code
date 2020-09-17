#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # left, right, res = 0, 0, 0
        # if not s:
        #     return res

        # n = len(s)
        # for i in range(n):
        #     if s[i] == '(':
        #         left += 1
        #     else:
        #         right += 1

        #     if left == right:
        #         res = max(res, 2 * right)
        #     elif left < right:
        #         left, right = 0, 0

        # left, right = 0, 0
        # for i in range(n - 1, -1, -1):
        #     if s[i] == ')':
        #         right += 1
        #     else:
        #         left += 1

        #     if left == right:
        #         res = max(res, 2 * left)
        #     elif left > right:
        #         left, right = 0, 0

        # return res

        # res = 0
        # if not s:
        #     return 0

        # n = len(s)
        # stack = [-1]
        # i = 0

        # while i < n:
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #         else:
        #             res = max(res, i - stack[-1])
        #     i += 1
        # return res

        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        res = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2]
                                         if i - dp[i - 1] - 2 >= 0 else 0) + 2
                res = max(res, dp[i])

        return res


# @lc code=end
