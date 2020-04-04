#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return None
        self.solve(board, 0)
    
    def solve(self, board: List[List[str]], row: int) -> bool:
        for i in range(row, 9):
            for j in range(9):
                # 待填数字
                if board[i][j] == '.':
                    for num in [str(i + 1) for i in range(9)]:
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board, row):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    
    def isValid(self, board: List[List[str]], row: int, column: int, number: str) -> bool:
        """
        Check current board
        """
        for i in range(9):
            # 横向
            if board[row][i] == number:
                return False
            # 纵向
            if board[i][column] == number:
                return False
            # 3 * 3 方格
            start_row = row // 3 * 3
            start_col = column // 3 * 3
            if board[start_row + i // 3][start_col + i % 3] == number:
                return False
        return True

        
# @lc code=end

