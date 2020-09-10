#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f = 1
        for i in range(2, n):
            f *= i
        nums = list(range(1, n+1))
        re = ''
        k -= 1
        while n > 1:
            index = k // f
            t = nums[index]
            re += str(t)
            nums.pop(index)
            k %= f
            n -= 1
            f //= n 
        return re + str(nums[0])
# @lc code=end

