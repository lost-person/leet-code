#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

# @lc code=start
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x, o = "XO"

        x_num = sum([b.count(x) for b in board])
        o_num = sum([b.count(o) for b in board])

        if o_num not in [x_num - 1, x_num]: return False

        def win(player, board):
            for i in range(3):
                if all([player == board[i][j] for j in range(3)]): return True
                if all([player == board[j][i] for j in range(3)]): return True

            if player == board[0][0] == board[1][1] == board[2][2]: return True
            if player == board[0][2] == board[1][1] == board[2][0]: return True

            return False

        if win(x, board) and x_num != o_num + 1: return False
        if win(o, board) and x_num != o_num: return False

        return True


# @lc code=end
