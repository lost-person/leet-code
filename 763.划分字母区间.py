#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S: return []
        if len(S) == 1: return [S]

        res = []
        char_dict = dict()
        for i, c in enumerate(S):
            char_dict[c] = i
        
        start, end = 0, 0
        for i, c in enumerate(S):
            end = max(end, char_dict[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
        

# @lc code=end

