#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 排序 直接返回
        # pass

        # 快排
        if not nums or not k:
            return -1
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            
            i = left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def select(left, right, k):
            if left == right:
                return nums[left]
            
            pivot_index = left
            pivot_index = partition(left, right, pivot_index)
            if pivot_index == k - 1:
                return nums[pivot_index]
            elif pivot_index < k - 1:
                return select(pivot_index + 1, right, k)
            else:
                return select(left, pivot_index - 1, k)
        
        return select(0, len(nums) - 1, k)


# @lc code=end

