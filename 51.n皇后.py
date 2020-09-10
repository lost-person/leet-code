#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int):
        solve_list = []
        queen = [None] * n

        def solve(queen, cur_row, n, solve_list):
            # 找到可行解
            if cur_row == n:
                # 替换
                solve_list.append(replace(queen))
                return
            
            for col in range(n):
                # 假设row, col 满足条件
                queen[cur_row], flag = col, True
                for row in range(cur_row):
                    # 判断是否满足（同一列，同一斜线）
                    if queen[row] == col or abs(col - queen[row]) == cur_row - row:
                        flag = False
                        break
                if flag:
                    solve(queen, cur_row + 1, n, solve_list)
        
        def replace(queen):
            res = []
            s = '.' * len(queen)
            for col in queen:
                res.append(s[:col] + 'Q' + s[col + 1:])
            return res

        solve(queen, 0, n, solve_list)
        return solve_list
        
# @lc code=end

