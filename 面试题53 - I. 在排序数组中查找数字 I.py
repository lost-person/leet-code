# coding = utf-8

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return 0 # 没有找到, 直接返回0
        idx1 = left
        
        # 如果这里能够运行, 肯定是找到了target的
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            # note that change to <=
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        # upper bound 应该是 right - 1
        # 返回 right - 1 - idx1 + 1
        # 退出循环时 left = right 
        return left - idx1

        def lower_bound(array, left, right, value):
            while left < right: # 返回[first, last)内第一个不小于value的值的位置
                mid = left + ((right - left) >> 1) # 搜索区间[first, last)不为空
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return array[left]

        def upper_bound(array, left, right, value):
            while left < right: # 返回[first, last)内第一个大于value的值的位置
                mid = left + ((right - left) >> 1) # 搜索区间[first, last)不为空
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            
            return array[left]

