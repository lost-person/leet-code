#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not n or k % n == 0: return

        k = k % n
        count = 0
        start = 0
        while count < n:
            prev = nums[start]
            current = start
            while True:
                next_index = (current + k) % n
                tmp = nums[next_index]
                nums[next_index] = prev
                prev = tmp
                current = next_index
                count += 1
                if start == current:
                    break
            start += 1

        # n = len(nums)
        # if not n or k % n == 0: return

        # k %= n

        # def reverse(start, end):
        #     while start < end:
        #         temp = nums[start]
        #         nums[start] = nums[end]
        #         nums[end] = temp
        #         start += 1
        #         end -= 1

        # reverse(0, n - 1)
        # reverse(0, k - 1)
        # reverse(k, n - 1)


# @lc code=endn
