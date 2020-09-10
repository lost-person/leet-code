#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

# @lc code=end

