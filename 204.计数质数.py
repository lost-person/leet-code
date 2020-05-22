#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime = [1] * n
        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = 0
                    j += i
            i += 1
        
        return sum(isPrime) - 2

# @lc code=end

