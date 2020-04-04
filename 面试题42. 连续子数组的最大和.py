# coding = utf-8

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        
        n = len(nums)
        if n < 2:
            return nums[0]
        
        res = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            res = max(res, nums[i])
        
        return res