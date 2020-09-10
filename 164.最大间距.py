#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0
        
        min_num, max_num = min(nums), max(nums)
        if min_num == max_num:
            return 0

        min_list = [0] * (n + 1)
        max_list = [0] * (n + 1)
        has_num = [False] * (n + 1)

        for num in nums:
            index = ((num - min_num) * n // (max_num - min_num))
            min_list[index] = num if not has_num[index] else min(min_list[index], num)
            max_list[index] = num if not has_num[index] else max(max_list[index], num)
            has_num[index] = True
        
        max_len = 0
        m = max_list[0]
        for i in range(1, n + 1):
            if has_num[i]:
                cur_len = min_list[i] - m
                max_len = max(max_len, cur_len)
                m = max_list[i]
        
        return max_len

# @lc code=end

