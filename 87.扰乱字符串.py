#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 递归方法
        # ans_dict = dict()
        # def solve(s1: str, s2: str) -> bool:
        #     ans = ans_dict.get(s1 + '#' + s2, -1)
        #     if ans == 1: return True
        #     if ans == 0: return False

        #     if s1 == s2: 
        #         ans_dict[s1 + '#' + s2] = 1
        #         return True
            
        #     m, n = len(s1), len(s2)
        #     if m != n:
        #         ans_dict[s1 + '#' + s2] = 0
        #         return False

        #     count = [0] * 26
        #     for c1, c2 in zip(s1, s2):
        #         count[ord(c1) - ord('a')] += 1
        #         count[ord(c2) - ord('a')] -= 1
            
        #     for i in range(len(count)):
        #         if count[i] != 0:
        #             ans_dict[s1 + '#' + s2] = 0
        #             return False

        #     for i in range(1, m):
        #         # 切割 s1，比较子树
        #         if solve(s1[i:], s2[i:]) and solve(s1[:i], s2[:i]):
        #             ans_dict[s1 + '#' + s2] = 1
        #             return True
        #         # 切割 s1，并交换，比较
        #         if solve(s1[i:], s2[:m-i]) and solve(s1[:i], s2[m-i:]):
        #             ans_dict[s1 + '#' + s2] = 1
        #             return True
            
        #     ans_dict[s1 + '#' + s2] = 0
        #     return False
        # return solve(s1, s2)

        # 动态规划
        l = len(s1)
        if l != len(s2): return False
        dp = [[None for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j] = [False] * (min(l-i, l-j)+1)
        for i in range(l):
            for j in range(l):
                dp[i][j][1] = s1[i] == s2[j]
        for length in range(2, l+1):
            for i in range(l-length+1):
                for j in range(l-length+1):
                    for sep in range(1, length): # 检查每一种子串划分的方法， sep 是分割的点
                        if dp[i][j][sep] and dp[i+sep][j+sep][length - sep]:      # 当前层两个子串未经过交换的情况
                            dp[i][j][length] = True
                            break
                        if dp[i][j+length-sep][sep] and dp[i+sep][j][length-sep]: # 当前层的两个子串经过交换的情况
                            dp[i][j][length] = True
                            break
        return dp[0][0][l]
# @lc code=end

