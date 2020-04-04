#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # if not n: return 1

        # res = [0] * (n + 1)
        # res[0], res[1] = 1, 1
        
        # for i in range(2, n + 1):
        #     for j in range(1, i + 1):
        #         res[i] += res[j - 1] * res[i - j]
        # return res[n]

        # 卡特兰数 C_{n + 1} = \frac{2(2n + 1)}{n + 2}C_{n}
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) // (i + 2)
        return C

# @lc code=end

