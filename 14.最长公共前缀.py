#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        trie_dict = trie.look_up
        res = ''
        while len(trie_dict) == 1:
            k, v = trie_dict.popitem()
            if k == '#':
                break
            res += k
            trie_dict = v
        return res

class Trie:
    def __init__(self):
        super().__init__()
        self.look_up = {}
    
    def insert(self, s: str):
        trie = self.look_up
        for c in s:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        # 结束符
        trie['#'] = '#'
 
# @lc code=end

