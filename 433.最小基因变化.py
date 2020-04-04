#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank or end not in bank: return -1
        if start == end: return 0
        gene_list = ['A', 'C', 'G', 'T']

        set1 = set()
        set2 = set()
        set1.add(start)
        set2.add(end)

        bank_set = set(bank)

        def bfs(set1: set, set2: set, bank_set, direction: bool, cnt: int):
            if len(set1) == 0:
                return -1
            if len(set1) > len(set2):
                return bfs(set2, set1, bank_set, not direction, cnt)
            
            bank_set = bank_set - set1 - set2
            done = False
            new_set = set()

            for word in set1:
                for i, c in enumerate(word):
                    for alpha in gene_list:
                        if c == alpha:
                            continue

                        tmp_word = word[:i] + alpha + word[i + 1:]
                        if tmp_word in set2:
                            return cnt

                        if tmp_word in bank_set:
                            new_set.add(tmp_word)
            
            return bfs(new_set, set2, bank_set, direction, cnt + 1)
        
        return bfs(set1, set2, bank_set, True, 1)
        
        
        # gene_set = set(bank)

        # def get_neightbors(word: str):
        #     neightbors = []
        #     for i, c in enumerate(word):
        #         for gene in gene_list:
        #             if gene == c: continue

        #             tmp_gene = word[:i] + gene + word[i + 1:]
        #             if tmp_gene in gene_set:
        #                 neightbors.append(tmp_gene)
        #     return neightbors

        # self.res = float('inf')
        
        # def bfs(start, end):
        #     visisted = set()
        #     visisted.add(start)
            
        #     path = [start]
        #     queue = deque()
        #     queue.append(path[:])
        #     is_found = False
            
        #     while queue:
        #         size = len(queue)
        #         subvisted = set()

        #         for i in range(size):
        #             path = queue.popleft()
        #             tmp_gene = path[-1]
        #             neightbors = get_neightbors(tmp_gene)
        #             for neightbor in neightbors:
        #                 if neightbor not in visisted:
        #                     if neightbor == end:
        #                         is_found = True
        #                         path.append(neightbor)
        #                         self.res = min(self.res, len(path) - 1)
        #                         path.pop()
                            
        #                     path.append(neightbor)
        #                     queue.append(path[:])
        #                     path.pop()
        #                     subvisted.add(neightbor)

        #         visisted = visisted | subvisted
        #         if is_found:
        #             break

        # bfs(start, end)
        # if self.res == float('inf'):
        #     self.res = -1
        # return self.res


# @lc code=end

