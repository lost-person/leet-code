#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pos1 = pos2 = 0
        n1, n2 = len(version1), len(version2)

        def get_next_chunk(version: str, n: int, p: int):
            if p > n - 1:
                return 0, p
            
            p_end = p
            while p_end < n and version[p_end] != '.':
                p_end += 1
            
            num = int(version[p:p_end]) if p_end < n else int(version[p:])
            p = p_end + 1

            return num, p

        while pos1 < n1 or pos2 < n2:
            num1, pos1 = get_next_chunk(version1, n1, pos1)
            num2, pos2 = get_next_chunk(version2, n2, pos2)
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
# @lc code=end

