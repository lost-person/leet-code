#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 这题太难了吧！！！
        res = []
        if not wordList or endWord not in wordList: return res
        
        def get_neightbors(word: str, word_set: set):
            neightbors = []
            for i, c in enumerate(word):
                for alpha_num in range(97, 124):
                    if c == chr(alpha_num): continue

                    tmp_word = word[:i] + chr(alpha_num) + word[i + 1:]
                    if tmp_word in word_set:
                        neightbors.append(tmp_word)
            
            return neightbors

        def bfs(beginWord: str, endWord: str, word_set: set):
            queue = deque()
            path = [beginWord]
            queue.append(path[:])

            isFound = False
            visited = set()
            visited.add(beginWord)

            while queue:
                size = len(queue)
                subVisited = set()

                for j in range(size):
                    p = queue.popleft()
                    tmp_word = p[-1]
                    neightbors = get_neightbors(tmp_word, word_set)
                    for neightbor in neightbors:
                        if neightbor not in visited:
                            if neightbor == endWord:
                                isFound = True
                                p.append(neightbor)
                                res.append(p[:])
                                p.pop()
                        
                            p.append(neightbor)
                            queue.append(p[:])
                            p.pop()
                            subVisited.add(neightbor)
                visited = visited | subVisited
                if isFound:
                    break
        
        bfs(beginWord, endWord, set(wordList))
        return res


    #     # 双向 bfs
    #     if not wordList or endWord not in wordList: return []

    #     self.word_dict = dict()
    #     self.bfs(beginWord, endWord, wordList)
        
    #     res = []

    #     def findLadders_helper(beginWord: str, endWord: str, tmp_res: list):
    #         if beginWord == endWord:
    #             res.append(tmp_res[:])
    #             return
            
    #         neightbors = self.word_dict.get(beginWord, [])
    #         for neightbor in neightbors:
    #             tmp_res.append(neightbor)
    #             findLadders_helper(neightbor, endWord, tmp_res)
    #             tmp_res.pop()
        
    #     findLadders_helper(beginWord, endWord, [beginWord])
    #     return res
    
    # def bfs(self, beginWord: str, endWord: str, wordList: list):
    #     set1 = set()
    #     set2 = set()
    #     word_set = set(wordList)
        
    #     set1.add(beginWord)
    #     set2.add(endWord)

    #     def bfs_helper(set1: set, set2: set, word_set: set, direction: bool):
    #         if len(set1) == 0:
    #             return False
            
    #         if len(set1) > len(set2):
    #             return bfs_helper(set2, set1, word_set, not direction)
            
    #         # 去除已经遍历的节点避免死循环
    #         word_set = word_set - set1 - set2

    #         done = False
    #         new_set = set()

    #         for word1 in set1:
    #             for i, c in enumerate(word1):
    #                 for alpha_num in range(97, 123):
    #                     # 相同字符
    #                     if c == chr(alpha_num):
    #                         continue
                        
    #                     # 获取邻接词
    #                     tmp_word = word1[:i] + chr(alpha_num) + word1[i + 1:]

    #                     # 因为一个自顶向下，另一个是自下向上，所以 k, v 相反
    #                     if direction:
    #                         key, value = word1, tmp_word
    #                     else:
    #                         key, value = tmp_word, word1
                        
    #                     tmp_list = self.word_dict.get(key, [])
                        
    #                     # 相遇
    #                     if tmp_word in set2:
    #                         done = True
    #                         tmp_list.append(value)
    #                         self.word_dict[key] = tmp_list
                        
    #                     # 没有相遇，但是是有效的邻接词，保存结果
    #                     if not done and tmp_word in word_set:
    #                         new_set.add(tmp_word)
    #                         tmp_list.append(value)
    #                         self.word_dict[key] = tmp_list
    #         return done or bfs_helper(set2, new_set, word_set, not direction)

    #     bfs_helper(set1, set2, word_set, True)
        

# @lc code=end

