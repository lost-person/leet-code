#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        left, right = 0, 0
        for i in range(n):
            right += nums[i]
            if left < nums[i]:
                left = nums[i]

        ans = right
        while left <= right:
            mid = left + ((right - left) >> 1)
            tmp_sum = 0
            cnt = 1
            for i in range(n):
                if tmp_sum + nums[i] > mid:
                    # 再次切分
                    cnt += 1
                    tmp_sum = nums[i]
                else:
                    tmp_sum += nums[i]
            
            if cnt <= m:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        # dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        # _sum = [0] * (n + 1)
        # for i in range(n):
        #     _sum[i + 1] = _sum[i] + nums[i]
        
        # dp[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         for k in range(i):
        #             dp[i][j] = min(dp[i][j], max(dp[k][j - 1], _sum[i] - _sum[k]))
        
        # return dp[n][m]

# @lc code=end

