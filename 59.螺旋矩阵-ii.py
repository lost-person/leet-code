#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        res = [[0] * n for _ in range(n)]
        if n == 0: return res

        num_list = range(1, n**2 + 1)
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        row, col, di = 0, 0, 0
        for i, num in enumerate(num_list):
            res[row][col] = num_list[i]
            
            next_row = row + dr[di]
            next_col = col + dc[di]

            if 0 <= next_row < n and 0 <= next_col <n and res[next_row][next_col] == 0:
                row, col = next_row, next_col
            
            else:
                di = (di + 1) % 4
                row += dr[di]
                col += dc[di]

        return res

# @lc code=end

