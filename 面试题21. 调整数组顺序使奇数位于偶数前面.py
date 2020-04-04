# coding = utf-8

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)

        low, high = 0, n - 1
        while low < high:
            while low < high and nums[low] & 1:
                low += 1
            while low < high and nums[high] & 1 == 0:
                high -= 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
        return nums
