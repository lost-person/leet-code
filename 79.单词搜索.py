#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not (board or board[0]): return False

        def dfs(i, j, word):
            if not word: return True
            # 超越边界
            if i < 0 or i == m or j < 0 or j == n: return False
            if board[i][j] != word[0]: return False

            # 避免重复使用
            board[i][j] += ' '
            res = dfs(i - 1, j, word[1:]) or dfs(i + 1, j, word[1:]) or dfs(i, j - 1, word[1:]) or dfs(i, j + 1, word[1:])
            board[i][j] = board[i][j][:-1]
            return res
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word): return True
        return False

        
# @lc code=end

