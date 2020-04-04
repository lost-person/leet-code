#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList: return 0

        set1 = set()
        set2 = set()
        word_set = set(wordList)
        
        set1.add(beginWord)
        set2.add(endWord)

        def bfs(set1: set, set2: set, word_set: set, direction: bool, cnt):
            if len(set1) == 0:
                return 0
            
            if len(set1) > len(set2):
                return bfs(set2, set1, word_set, not direction, cnt)
            
            # 去除已经遍历的节点避免死循环
            word_set = word_set - set1 - set2

            new_set = set()

            for word1 in set1:
                for i, c in enumerate(word1):
                    for alpha_num in range(97, 123):
                        # 相同字符
                        if c == chr(alpha_num):
                            continue
                        
                        # 获取邻接词
                        tmp_word = word1[:i] + chr(alpha_num) + word1[i + 1:]
                        
                        # 相遇
                        if tmp_word in set2:
                            return cnt
                        
                        # 没有相遇，但是是有效的邻接词，保存结果
                        if tmp_word in word_set:
                            new_set.add(tmp_word)

            return bfs(set2, new_set, word_set, not direction, cnt + 1)

        return bfs(set1, set2, word_set, True, 2)

# @lc code=end

