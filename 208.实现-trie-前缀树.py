#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look_up = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.look_up
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        # 单词结束标志
        tree["#"] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.look_up
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if '#' in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.look_up
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

if __name__ == "__main__":
    trie = Trie()
    trie.insert("oath")
    trie.insert("pea")
    trie.insert("eat")
    trie.insert("ain")
    trie.insert("apple")
    trie.insert("appl")
    trie.search("apple")
    trie.search("app")
    trie.startsWith("app")
    trie.insert("app")  
    trie.search("app")

