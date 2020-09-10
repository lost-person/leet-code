#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        # 判断所在行
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
# @lc code=end

