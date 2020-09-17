#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        times = len(s) // 4

        # 将counter修剪成键值对中值大于times的字典
        for k in list(counter.keys()):
            if counter[k] > times:
                counter[k] = counter[k] - times
            else:
                del counter[k]

        # 此时的counter是平衡字符串需要改进的字符
        # 如果counter为0表示每个元素都符合平衡字符串
        if len(counter) == 0:
            return 0

        # 在s中找出连续的字串，字串必须包含counter所有的元素，顺序没有要求
        window = defaultdict(int)
        left, right, n = 0, 0, len(s)
        match, minlength = 0, float('inf')

        while right < n:
            c1 = s[right]
            # 如果right元素在counter中
            if c1 in counter:
                window[c1] += 1
                if window[c1] == counter[c1]:
                    # 能够匹配时，匹配数加一
                    match += 1
            right += 1
            # 如果可以匹配，left += 1，寻找匹配时的最优子字符串
            while match == len(counter):
                # 更新最优子字符串的长度
                if right - left <= minlength:
                    minlength = right - left
                c2 = s[left]
                if c2 in counter:
                    window[c2] -= 1
                    if window[c2] < counter[c2]:
                        match -= 1
                left += 1
        return minlength


# @lc code=end
