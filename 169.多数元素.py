#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 哈希表
        # if not nums: return 0

        # half_n = len(nums) >> 1
        # num_dict = dict()
        # for num in nums:
        #     num_dict[num] = num_dict.get(num, 0) + 1
        
        # for k, v in num_dict.items():
        #     if v > half_n:
        #         return k

        # 排序
        # nums.sort()
        # return nums[len(nums) >> 1]

        # 分治
        # def majority_element_rec(lo, hi):
        #     # base case; the only element in an array of size 1 is the majority
        #     # element.
        #     if lo == hi:
        #         return nums[lo]

        #     # recurse on left and right halves of this slice.
        #     mid = (hi-lo) // 2 + lo
        #     left = majority_element_rec(lo, mid)
        #     right = majority_element_rec(mid+1, hi)

        #     # if the two halves agree on the majority element, return it.
        #     if left == right:
        #         return left

        #     # otherwise, count each element and return the "winner".
        #     left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        #     right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

        #     return left if left_count > right_count else right

        # return majority_element_rec(0, len(nums)-1)

        # 投票法
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# @lc code=end

