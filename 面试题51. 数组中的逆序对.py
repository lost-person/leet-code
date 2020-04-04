# coding = utf-8

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.cnt = 0
        
        def merge(nums, start, mid, end, temp):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            temp.clear()
                    

        def mergeSort(nums, start, end, temp):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid + 1, end, temp)
            merge(nums, start, mid,  end, temp)
        mergeSort(nums, 0, len(nums) - 1, [])
        return self.cnt
