# coding = utf-8

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a or len(a) < 2:
            return []
        
        n = len(a)

        # 左向右
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * a[i - 1]
        
        # 右向左
        R = 1
        for i in range(n - 1, -1, -1):
            res[i] *= R
            R *= a[i]
        
        return res
