#
# @lc app=leetcode.cn id=1452 lang=python3
#
# [1452] 收藏清单
#

# @lc code=start
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        return [i for i, f in enumerate(favoriteCompanies) if not any(set(c) > set(f) for c in favoriteCompanies)]
# @lc code=end

