#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res_list = []
        if not matrix: return res_list

        m = len(matrix)
        n = len(matrix[0])

        seen = [[False] * n for _ in matrix]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        row, col, di = 0, 0, 0
        for _ in range(m * n):
            res_list.append(matrix[row][col])
            seen[row][col] = True

            next_row = row + dr[di]
            next_col = col + dc[di]
            if 0 <= next_row < m and 0 <= next_col < n and not seen[next_row][next_col]:
                row = next_row
                col = next_col
            else:
                di = (di + 1) % 4
                row += dr[di]
                col += dc[di]

        return res_list
# @lc code=end

