#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        # 因为不会在边界
        if m <= 2 or n <= 2: return

        # def dfs(i, j):
        #     """递归
        #     """
        #     if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] == 'X' or board[i][j] == '#':
        #         return
            
        #     board[i][j] = '#'
        #     dfs(i - 1, j)
        #     dfs(i, j - 1)
        #     dfs(i + 1, j)
        #     dfs(i, j + 1)

        # def dfs(i, j):
        #     """非递归
        #     """
        #     board[i][j] = "#"
        #     tmp_list = [(i, j)]
        #     while tmp_list:
        #         cur_i, cur_j = tmp_list[-1]

        #         # 上
        #         if cur_i - 1 >= 0 and board[cur_i - 1][cur_j] == 'O':
        #             board[cur_i - 1][cur_j] = '#'
        #             tmp_list.append((cur_i - 1, cur_j))
        #             continue
        #         # 下
        #         if cur_i + 1 < m and board[cur_i + 1][cur_j] == 'O':
        #             board[cur_i + 1][cur_j] = "#"
        #             tmp_list.append((cur_i + 1, cur_j))
        #             continue
        #         # 左
        #         if cur_j - 1 >= 0 and board[cur_i][cur_j - 1] == 'O':
        #             board[cur_i][cur_j - 1] = "#"
        #             tmp_list.append((cur_i, cur_j - 1))
        #             continue
        #         # 右
        #         if cur_j + 1 < n and board[cur_i][cur_j + 1] == 'O':
        #             board[cur_i][cur_j + 1] = "#"
        #             tmp_list.append((cur_i, cur_j + 1))
        #             continue
        #         tmp_list.pop()
        
        def bfs(i, j):
            """非递归
            """
            board[i][j] = "#"
            tmp_list = [(i, j)]
            while tmp_list:
                cur_i, cur_j = tmp_list.pop()

                # 上
                if cur_i - 1 >= 0 and board[cur_i - 1][cur_j] == 'O':
                    board[cur_i - 1][cur_j] = '#'
                    tmp_list.append((cur_i - 1, cur_j))
                # 下
                if cur_i + 1 < m and board[cur_i + 1][cur_j] == 'O':
                    board[cur_i + 1][cur_j] = "#"
                    tmp_list.append((cur_i + 1, cur_j))
                # 左
                if cur_j - 1 >= 0 and board[cur_i][cur_j - 1] == 'O':
                    board[cur_i][cur_j - 1] = "#"
                    tmp_list.append((cur_i, cur_j - 1))
                # 右
                if cur_j + 1 < n and board[cur_i][cur_j + 1] == 'O':
                    board[cur_i][cur_j + 1] = "#"
                    tmp_list.append((cur_i, cur_j + 1))

        
        # 遍历
        for i in range(0, m):
            for j in range(0, n):
                if not (0 < i < m - 1 and 0 < j < n - 1) and board[i][j] == 'O':
                    bfs(i, j)
        
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == '#':
                    board[i][j] = 'O'
        
# @lc code=end

