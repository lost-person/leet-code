#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿法迭代
        # if x <= 1: return x
        # r = x
        # tmp_r = x / r
        # while r > tmp_r:
        #     r = (r + tmp_r) // 2
        #     tmp_r = x / r
        # return int(r)

        # 二分法
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left
# @lc code=end

