# coding = utf-8

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        min_ = 14
        max_ = 0
        overlapNumber = [0] * 15 #记录有无重复元素出现
        for i in range(5):
            if nums[i] == 0:# 遇到大小王则跳过
                continue
            if overlapNumber[nums[i]]:#存在重复元素则不符合条件
                return False
            overlapNumber[nums[i]] = 1 #记录已经出现过的元素
            min_ = min(min_, nums[i])# 更新最小值
            max_ = max(max_, nums[i])# 更新最大值
        return max_ - min_ + 1 <= 5 #判断
