# coding = utf-8
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return -1
        
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            while left < right and numbers[left] == numbers[left + 1]: left += 1
            while left < right and numbers[right] == numbers[right - 1]: right -= 1
            
            mid = left + ((right - left) >> 1)
            
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                mid = right
        
        return numbers[left]
