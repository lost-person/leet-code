#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # # 二分法
        # if num < 2: return True

        # left, right = 2, num >> 1

        # while left <= right:
        #     mid = left + ((right - left) >> 1)
        #     mid_squre = mid * mid
        #     if mid_squre == num: return True
        #     elif mid_squre > num:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return False

        # 牛顿迭代法
        if num < 2: return True

        x = num >> 1
        while x * x > num:
            x = (x + num // x) >> 1
        return x * x == num
# @lc code=end

