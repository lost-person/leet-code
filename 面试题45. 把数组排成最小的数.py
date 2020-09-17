# coding = utf-8
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])

        num_list = [[] for _ in range(10)]

        # 根据高位判断
        for num in nums:
            num = str(num)
            first_num = int(num[0])
            num_list[first_num].append(num)

        def quick_sort(data, left, right):
            """自定义快排
            """
            if right - left < 1:
                return
            p = left
            q = right
            temp = data[left]
            while p < q:
                while p < q and temp + data[q] < data[q] + temp:
                    q -= 1
                if p < q:
                    data[p] = data[q]
                    p += 1
                while p < q and data[p] + temp < temp + data[p]:
                    p += 1
                if p < q:
                    data[q] = data[p]
                    q -= 1
            data[p] = temp
            quick_sort(data, left, p - 1)
            quick_sort(data, p + 1, right)

        res = ''

        for i in range(10):
            if num_list[i] == []:
                continue
            quick_sort(num_list[i], 0, len(num_list[i]) - 1)
            for num in num_list[i]:
                res += num

        return res
