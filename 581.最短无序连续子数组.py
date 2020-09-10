#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 排序之后比较（略）
        res = 0
        if not nums or len(nums) == 1:
            return res
        
        n = len(nums)
        num_min, num_max = float('inf'), float('-inf')
        for i in range(0, n - 1):
            # 局部无序
            if nums[i] > nums[i + 1]:
                num_max = max(num_max, nums[i])
                num_min = min(num_min, nums[i + 1])
        
        start, end = 0, 0
        for i in range(n):
            if nums[i] > num_min:
                start = i
                break
        
        for i in range(n - 1, -1, -1):
            if nums[i] < num_max:
                end = i
                break
        
        return end - start + 1 if start or end else 0

        # stack = []
        # start, end = n - 1, 0
        # for i in range(n):
        #     while stack and nums[stack[-1]] > nums[i]:
        #         start = min(start, stack.pop())
        #     stack.append(i)
        
        # stack.clear()

        # for i in range(n - 1, -1, -1):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         end = max(end, stack.pop())
        #     stack.append(i)
        
        # return end - start + 1 if end > start else 0
# @lc code=end

