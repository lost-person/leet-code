# coding = utf-8

import sys
from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        Q, W, E, R = "QWER"
        char_dict = {Q: 0, W: 0, E: 0, R: 0}

        res = 0
        n = len(s)
        limit = n // 4

        for c in s:
            char_dict[c] += 1

        for k, v in char_dict.items():
            if v < limit: continue

            res += v - limit
        
        return res
        
    
s = Solution()
print(s.balancedString("WWEQERQWQWWRWWERQWEQ"))
