#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ## 超时
        # if len(s3) != (len(s1) + len(s2)): return False

        # def is_interleave(s1_i, s2_j, s3_k):
        #     if not s3_k: return True

        #     res_1, res_2 = False, False
        #     if s1_i and s1_i[0] == s3_k[0]:
        #         res_1 = is_interleave(s1_i[1:], s2_j, s3_k[1:])
        #     if s2_j and s2_j[0] == s3_k[0]:
        #         res_2 = is_interleave(s1_i, s2_j[1:], s3_k[1:])
        #     return res_1 or res_2
        # return is_interleave(s1, s2, s3)

        ## 二维 dp
        # m, n, l = len(s1), len(s2), len(s3)
        # if l != (m + n): return False

        # res = [[False] * (n + 1) for _ in range(m + 1)]
        # res[0][0] = True

        # i, j = 0, 0
        # for i in range(1, m + 1):
        #     res[i][0] = res[i - 1][0] and (s1[i - 1] == s3[i - 1])

        # for j in range(1, n + 1):
        #     res[0][j] = res[0][j - 1] and (s2[j - 1] == s3[j - 1])

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         res[i][j] = (res[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
        #             res[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        # return res[m][n]

        ## 一维 dp
        m, n, l = len(s1), len(s2), len(s3)
        if l != (m + n): return False

        res = [False] * (n + 1)
        res[0] = True if s1 == s3 else False
        for j in range(1, n + 1):
            res[j] = res[j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 and j == 0:
                    res[j] = True
                elif i == 0:
                    res[j] = res[j - 1] and (s2[j - 1] == s3[j - 1])
                elif j == 0:
                    res[j] = res[j] and (s1[i - 1] == s3[i - 1])
                else:
                    res[j] = (res[j] and s1[i - 1] == s3[i + j - 1]) or (
                        res[j - 1] and s2[j - 1] == s3[i + j - 1])
        return res[n]


# @lc code=end
