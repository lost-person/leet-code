# coding = utf-8

from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return []

        n = len(arr)
        if n <= k:
            return arr

        def partition(low, high, pivot_index):
            """快排划分
            """
            pivot = arr[pivot_index]
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1

            arr[j] = pivot
            return j

        def select(low, high, k):
            if low == high:
                return arr[:k]

            pivot_index = low
            pivot_index = partition(low, high, pivot_index)
            if pivot_index == k - 1:
                return arr[:k]
            elif pivot_index < (k - 1):
                return select(pivot_index + 1, high, k)
            else:
                return select(low, pivot_index - 1, k)

        return select(0, n - 1, k)
