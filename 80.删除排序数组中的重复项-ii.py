#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        # n = len(nums)
        # cnt = 1
        # for i in range(n - 2, -1, -1):
        #     if nums[i] == nums[i + 1]:
        #         cnt += 1
        #     else:
        #         cnt = 1
        #     if cnt > 2:
        #         nums.pop(i - n)
        #         n -= 1
        
        # return len(nums)

        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i
# @lc code=end

