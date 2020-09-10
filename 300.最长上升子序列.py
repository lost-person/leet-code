#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return n
        
        # dp
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        # 二分加dp
        dp, res = [0] * n, 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = i + ((j - i) >> 1)
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res
# @lc code=end

