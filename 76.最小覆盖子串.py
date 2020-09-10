#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        # 统计 t 中各字符及其数量
        dict_t = Counter(t)
        required = len(dict_t)
        
        # 窗口
        window = {}
        left, right = 0, 0
        formed = 0
        
        filter_s = []
        # 统计 s 中 t 个字符的对应位置
        for i, c in enumerate(s):
            if c in dict_t:
                filter_s.append((i, c))
        
        ans = float("inf"), None, None
        # 确定满足条件的窗口，即窗口内字符及其数量与t中相同
        while right < len(filter_s):
            c = filter_s[right][1]
            window[c] = window.get(c, 0) + 1

            if window[c] == dict_t[c]:
                formed += 1
            
            # 缩小窗口
            while left <= right and formed == required:
                c = filter_s[left][1]

                start = filter_s[left][0]
                end = filter_s[right][0]
                if end - start < ans[0]:
                    ans = (end - start + 1, start, end + 1)
                
                # 更新窗口
                window[c] -= 1
                if window[c] < dict_t[c]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]]
# @lc code=end

