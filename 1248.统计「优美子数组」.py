#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        if not nums or len(nums) < k: return res

        n = len(nums)
        left, right = 0, 0
        odd_cnt = 0
        while right < n:
            if (nums[right] & 1) == 1:
                odd_cnt += 1
            
            right += 1

            if odd_cnt == k:
                tmp = right
                
                while right < n and (nums[right] & 1) == 0:
                    right += 1
                right_event_cnt = right - tmp + 1

                left_event_cnt = 0
                while left < right and (nums[left] & 1) == 0:
                    left_event_cnt += 1
                    left += 1

                left += 1
                odd_cnt -= 1
                res += (left_event_cnt + 1) * right_event_cnt    

        return res
# @lc code=end

