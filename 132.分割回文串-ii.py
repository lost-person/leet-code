#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#


# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        if not s: return 0

        n = len(s)
        checkPalindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            checkPalindrome[i][i] = True

        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2
                                     or checkPalindrome[i + 1][j - 1]):
                    checkPalindrome[i][j] = True

        dp = list(range(n))

        for i in range(1, n):
            if checkPalindrome[0][i]:
                dp[i] = 0
                continue

            dp[i] = min(dp[j] + 1 for j in range(i)
                        if checkPalindrome[j + 1][i])

        return dp[n - 1]

        # if not s: return 0
        # n = len(s)
        # if n < 2: return 0

        # checkPalindrome = list(range(n))

        # for i in range(1, n):
        #     if s[: i + 1] == s[: i + 1][::-1]:
        #         checkPalindrome[i] = 0
        #         continue

        #     checkPalindrome[i] = min(checkPalindrome[j] + 1 for j in range(i) if s[j + 1: i + 1] == s[j + 1: i + 1][::-1])

        # return checkPalindrome[n - 1]


# @lc code=end
