#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        
        res = []
        for word in words:
            x = word.lower()
            setx = set(x)
            if setx <= set1 or setx <= set2 or setx <= set3:
                res.append(word)
        
        return res
# @lc code=end

