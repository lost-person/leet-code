# coding = utf-8

from typing import List

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return -1

        def get_answer(nums, left, right):
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            left_ans = get_answer(nums, left, mid - 1)
            
            if left_ans != -1:
                return left_ans
            
            elif nums[mid] == mid:
                return nums[mid]
            else:
                return get_answer(nums, mid + 1, right)
            
        return get_answer(nums, 0, len(nums) - 1)