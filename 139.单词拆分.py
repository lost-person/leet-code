#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 暴力递归，超时，不过应该可以优化
        # if not wordDict: return False

        # word_set = set(wordDict)

        # def backtrack(start: int):
        #     if start == len(s):
        #         return True
            
        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in word_set and backtrack(end):
        #             return True
            
        #     return False
        # return backtrack(0)

        # # 树
        # if not wordDict: return False

        # word_set = set(wordDict)
        # n = len(s)
        # visited = [False] * n
        # queue = [0]
        
        # while queue:
        #     start = queue.pop()
        #     if not visited[start]:
        #         for end in range(start + 1, n + 1):
        #             if s[start: end] in word_set:
        #                 if end == n:
        #                     return True
        #                 queue.append(end)
        #         visited[start] = True

        # return False
                    
        # 动态规划
        if not wordDict: return False

        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n] 

# @lc code=end

