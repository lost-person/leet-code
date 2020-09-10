# coding = utf-8

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 1

        num = str(num)
        length = len(num)
        dp = [0] * (length + 1)
        dp[0] = dp[1] = 1
        for i in range(2, length + 1):
            dp[i] = dp[i - 1] + (dp[i - 2] if num[i - 2] != '0' and num[i - 2:i] < '26' else 0)

        return dp[-1]
