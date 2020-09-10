#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [0, 0]
        
        left, right = 0, len(numbers) - 1
        while left < right:            
            if numbers[left] == target - numbers[right]:
                return [left + 1, right + 1]

            elif numbers[left] < target - numbers[right]:
                left += 1
            
            else:
                right -= 1
        return [0, 0]
# @lc code=end

