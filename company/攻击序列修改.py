# coding = utf-8

def solve(s: str) -> int:
    if not s: return 0

    n = len(s)
    if n & 1: return -1

    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def dp_helper(left, right):
        if left >= right: return 0
        if dp[left][right] != -1: return dp[left][right]

        res = float("inf")
        ok = 0 if s[left] == "K" else 1

        for i in range(left + 1, right, 2):
            if s[i] == "J":
                res = min(res, dp_helper(left + 1, i) + dp_helper(i + 1, right) + ok)
            else:
                res = min(res, dp_helper(left + 1, i) + dp_helper(i + 1, right) + 1 + ok)
        
        dp[left][right] = res
        return dp[left][right]
    
    return dp_helper(0, n)

print(solve("JK"))