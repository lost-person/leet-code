# coding = utf-8

from typing import List


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

        # # 快慢指针
        # slow, fast = 0, 0
        # while fast < n:
        #     if nums[fast] & 1:
        #         nums[slow], nums[fast] = nums[fast], nums[slow]
        #         slow += 1
        #     fast += 1
        # return nums

        # # 相对顺序不变
        # while i < n:
        #     if nums[i] & 1 == 0:
        #         j = i + 1
        #         while j < n and nums[j] & 1:
        #             j += 1
                
        #         if j == n: break

        #         odd_num = nums[j]
        #         while j > i:
        #             nums[j] = nums[j - 1]
        #             j -= 1
        #         nums[j] = odd_num

        #     i += 1