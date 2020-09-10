#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        num_set = set(nums)
        long_strike = 0

        for num in nums:
            if num - 1 not in num_set:
                cur_num = num
                cur_long_strike = 1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_long_strike += 1
                
                long_strike = max(long_strike, cur_long_strike)
        
        return long_strike
# @lc code=end

