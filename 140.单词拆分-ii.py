#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 递归
        if not s:
            return []
        _len, wordDict = len(s), set(wordDict)
        _min, _max = 2147483647, -2147483648
        for word in wordDict:
            _min = min(_min, len(word))
            _max = max(_max, len(word))

        def dfs(start):  # 返回s[start:]能由字典构成的所有句子
            if start not in memo:
                res = []
                for i in range(_min, min(_max, _len - start) + 1):
                    if s[start:start + i] in wordDict:
                        res.extend(
                            list(
                                map(lambda x: s[start:start + i] + ' ' + x,
                                    dfs(start + i))))
                memo[start] = res
            return memo[start]

        memo = {_len: ['']}
        return list(map(lambda x: x[:-1], dfs(0)))

        # dp
        # res = []
        # if not wordDict: return []

        # word_set = set(wordDict)
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True

        # for i in range(1, n + 1):
        #     for j in range(0, i):
        #         if dp[j] and s[j: i] in word_set:
        #             dp[i] = True
        #             break

        # queue = collections.deque()

        # def dfs(end):
        #     if s[: end] in wordDict:
        #         queue.appendleft(s[: end])
        #         res.append(' '.join(queue))
        #         queue.popleft()

        #     for i in range(1, end):
        #         if dp[i]:
        #             suffix = s[i: end]
        #             if suffix in word_set:
        #                 queue.appendleft(suffix)
        #                 dfs(i)
        #                 queue.popleft()

        # if dp[-1]:
        #     dfs(n)
        # return res


# @lc code=end
