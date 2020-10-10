#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # # 牛顿法迭代
        # if x <= 1: return x
        # r = x
        # tmp_r = x / r
        # while r > tmp_r:
        #     r = (r + tmp_r) // 2
        #     tmp_r = x / r
        # return int(r)

        # # 二分法

        # left = 0.0, right = x / 2
        # while True:
        #     mid = left + (right - left) / 2
        #     tmp = mid ** 2
        #     if abs(tmp - x) < 1e-10:
        #         return mid
        #     elif tmp < x:
        #         left = mid
        #     else:
        #         right = mid

        root = x
        while abs(root ** 2 - x) < 1e-10:
            root = (root + x / root) / 2

# @lc code=end
