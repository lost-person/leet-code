# coding = utf-8

from typing import List

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr or len(arr) == 0: return -1

        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[left] < arr[mid]:
                if arr[left] <= target and target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] > arr[mid]:
                if arr[left] <= target or target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if arr[left] != target:
                    left += 1
                else:
                    right = left
        return left if arr[left] == target else -1
