#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class UglyNumber:
    def __init__(self):
        super().__init__()
        i2, i3, i5 = 3, 2, 1
        self.nums = list(range(1, 7))

        for i in range(6, 1690):
            ugly = min(self.nums[i2] * 2, self.nums[i3] * 3, self.nums[i5] * 5)
            self.nums.append(ugly)

            if ugly % 2 == 0:
                i2 += 1
            
            if ugly % 3 == 0:
                i3 += 1
            
            if ugly % 5 == 0:
                i5 += 1

class Solution:
    ugly_number= UglyNumber()
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0

        if n <= 6:
            return n
        
        return self.ugly_number.nums[n - 1]

# @lc code=end

