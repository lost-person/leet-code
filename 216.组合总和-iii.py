#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        if k == 0 or n == 0:
            return res

        def backtrack(candidates: List[int], cur: List[int], target: int, length: int):
            if len(cur) == length and target == 0:
                res.append(cur[:])
                return
            
            for i, candidate in enumerate(candidates):
                if len(cur) > 0 and candidate < cur[-1]:
                    continue
                
                cur.append(candidate)
                backtrack(candidates[i + 1:], cur, target - candidate, length)
                cur.pop()
        
        candidates = list(range(1, 10))
        backtrack(candidates, [], target=n, length=k)
        return res
# @lc code=end

