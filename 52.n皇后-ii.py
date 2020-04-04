#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        queen = [None] * n

        def solve(queen, cur_row, n, res):
            # 找到可行解
            if cur_row == n:
                # 替换
                res += 1
                return res
            
            for col in range(n):
                # 假设row, col 满足条件
                queen[cur_row], flag = col, True
                for row in range(cur_row):
                    # 判断是否满足（同一列，同一斜线）
                    if queen[row] == col or abs(col - queen[row]) == cur_row - row:
                        flag = False
                        break
                if flag:
                    res = solve(queen, cur_row + 1, n, res)
            
            return res

        res = solve(queen, 0, n, res)
        return res
        
# @lc code=end

