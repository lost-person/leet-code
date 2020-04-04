# coding = utf-8

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if not n:
            return []
        
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
        
        return list(range(1, my_pow(10, n)))
