#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#

# @lc code=start
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        mask = 0

        for i in range(30, -1, -1):
            # 高位到低位
            mask |= (1 << i)
            s = set()

            # 保留前缀
            for num in nums:
                s.add(num & mask)

            tmp = res | (1 << i)

            for prefix in s:
                if tmp ^ prefix in s:
                    res = tmp
                    break

        return res


# @lc code=end
