#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        n = len(nums)
        # 无需跳跃
        if n == 0: return res
        
        index = 0
        while index < n:
            # 抵达终点
            if nums[index] + index >= n - 1:
                res = True
                break
            
            if nums[index] == 0:
                break

            # 寻找最优的下一步
            next_index = index
            dist = 0
            for i in range(1, nums[index] + 1):
                if nums[index + i] + i > dist:
                    dist = nums[index + i] + i
                    next_index = index + i

            index = next_index
        return res
# @lc code=end

