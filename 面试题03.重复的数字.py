# coding = utf-8
class Solution:
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序（略）
        # 哈希表（略）
        # 下标法
        # for index, value in enumerate(nums):
        #     while index != value:
        #         # 出现重复
        #         if nums[value] == value:
        #             return value
        #         nums[value], nums[index] = nums[index], nums[value]
        # return -1

        # 分治
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            mid = left + ((right - left) >> 1)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
