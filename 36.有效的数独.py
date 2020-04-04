#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    seen += (i, board[i][j]),(board[i][j], j),(i//3, j//3, board[i][j])
        return len(seen) == len(set(seen))

# @lc code=end

