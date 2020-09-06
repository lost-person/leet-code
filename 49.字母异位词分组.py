#
# @lc app=leetcode.cn id=49 lang=python3
# coding=utf-8
# [49] 字母异位词分组
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # 字符串排序
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()

        # 统计字符数
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
# @lc code=end

