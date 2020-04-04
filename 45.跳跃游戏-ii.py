#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        n = len(nums)
        # 无需跳跃
        if n <= 1: return step
        
        index = 0
        while index < n:
            # 抵达终点
            if nums[index] + index >= n - 1:
                return step + 1
            
            # 寻找最优的下一步
            next_index = index
            dist = 0
            for i in range(1, nums[index] + 1):
                if nums[index + i] + i > dist:
                    dist = nums[index + i] + i
                    next_index = index + i
            
            step += 1
            index = next_index

        return step
        
# @lc code=end

