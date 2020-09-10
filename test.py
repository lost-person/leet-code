# coding = utf-8

import sys

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        init_state = [0, 0, 0]
        res = [-1] * len(requirements)

        for i, _increase in enumerate(increase):
            init_state = list(map(lambda x, y: x + y, init_state, _increase))
            for j, _requirement in enumerate(requirements):
                if res[j] == -1 and all(map(lambda x, y: x > y, init_state, _requirement)):
                    res[j] = i + 1

        return res
