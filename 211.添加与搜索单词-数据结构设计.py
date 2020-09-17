#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        for c in word:
            cur_node = cur_node.children[c]
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur_node = self.root

        def _helper(node, word, index):
            if index == len(word):
                return node.is_word

            cur_node = node
            c = word[index]
            if c == '.':
                for node in cur_node.children.values():
                    if _helper(node, word, index + 1):
                        return True
                return False
            else:
                cur_node = cur_node.children.get(c)
                if not cur_node:
                    return False
                return _helper(cur_node, word, index + 1)

        return _helper(cur_node, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
