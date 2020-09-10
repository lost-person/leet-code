#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 二分法
        if n < 0: 
            x = 1 / x
            n = -n
        
        res = 1
        cur_prod = x
        i = n
        while i > 0:
            if i % 2 == 1:
                res *= cur_prod
            cur_prod *= cur_prod
            
            i = i // 2 
        return res
        # def fastPow(x:float, n: int) -> float:
        #     if n == 0: return 1
        #     if n == 1: return x
            
        #     hal_res = fastPow(x, n // 2)

        #     if n % 2 != 0:
        #         res = x * hal_res * hal_res
        #     else:
        #         res = hal_res * hal_res
        #     return res   
        
        # return fastPow(x, n)
        
# @lc code=end

