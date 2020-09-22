# coding = utf-8

from typing import List

def solve(num: int, bowl: List[int]) -> int:
    if num <= 2 or len(bowl) <= 2: return -1
    return (bowl[0] + bowl[-1]) * (num + 1) // 2 - sum(bowl)
