# coding = utf-8
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        
        def my_pow(x: float, n: int):
            if n == 0:
                return 1

            if n == 1:
                return x
            
            odd = n & 1
            n >>= 1
            if odd:
                return x * my_pow(x, n) * my_pow(x, n)
            else:
                return my_pow(x, n) * my_pow(x, n)
        
        return my_pow(x, n)
