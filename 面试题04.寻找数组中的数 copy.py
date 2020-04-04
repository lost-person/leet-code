# coding = utf-8
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        # m, n = len(matrix), len(matrix[0])

        # row, col = m - 1, 0
        # while row >= 0 and col < n:
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         col += 1
        #     else:
        #         row -= 1
        # return False

        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False

        # 从右上角开始查找
        x = 0
        y = cols - 1

        while x < rows and y >= 0:
            # 1、从右到左，找第 1 个小于或者等于 target 的数
            if y == 0 and matrix[x][0] > target:
                return False
            left = 0
            right = y
            while left < right:
                mid = left + (right - left + 1) // 2
                if matrix[x][mid] <= target:
                    left = mid
                else:
                    # assert array[x][mid] > target
                    right = mid - 1

            y = left
            # 2、从上到下，找第 1 个大于或者等于 target 的数
            if x == rows - 1 and matrix[rows - 1][y] < target:
                return False

            left = x
            right = rows - 1
            while left < right:
                mid = left + (right - left) // 2
                if matrix[mid][y] >= target:
                    right = mid
                else:
                    # assert array[mid][y] < target
                    left = mid + 1
            x = left

            if matrix[x][y] == target:
                return True

        return False
