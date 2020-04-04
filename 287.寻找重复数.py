#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or not nums:
            return -1

        # 排序
        # nums.sort()
        # pre_num = nums[0]
        # for num in nums[1:]:
        #     if pre_num == num:
        #         return pre_num
        #     pre_num = num
        # return -1

        # n = len(nums)
        # left = 1
        # right = n - 1
        
        # while left < right:
        #     mid = left + ((right - left) >> 1)
        #     cnt = 0
        #     for num in nums:
        #         if num <= mid:
        #             cnt += 1
            
        #     if cnt > mid:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return left

        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1

# @lc code=end

