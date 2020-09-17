#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        if not board or not board[0] or not words:
            return res

        # 构建前缀树
        trie = {}
        for word in words:
            t = trie
            for c in word:
                t = t.setdefault(c, {})
            t['end'] = 1

        res = []
        m, n = len(board), len(board[0])
        coordinate_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, trie, s):
            c = board[row][col]
            if c not in trie:
                return

            trie = trie[c]
            if 'end' in trie and trie['end'] == 1:
                res.append(s + c)
                trie['end'] = 0
            board[row][col] = '#'

            for coordinate in coordinate_list:
                new_row = row + coordinate[0]
                new_col = col + coordinate[1]
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][
                        new_col] != '#':
                    dfs(new_row, new_col, trie, s + c)

            board[row][col] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")

        return res


# @lc code=end
