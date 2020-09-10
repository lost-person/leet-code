#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []

        if not people or not people[0]:
            return res
        
        people.sort(key = lambda x: (-x[0], x[1]))
        for p in people:
            res.insert(p[1], p)
        
        return res
# @lc code=end

