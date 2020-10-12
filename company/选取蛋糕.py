# coding = utf-8

def solve():
    n, m, a, b = map(int, input().split())
    cake_list = list(map(int, input().split()))

    if a > b:
        a, b = b, a

    need_cake = 2
    for cake in cake_list:
        if cake < a or cake > b:
            return "NO"
        
        if cake == a:
           need_cake -= 1
        
        if cake == b:
           need_cake -= 1

    return "YES" if need_cake <= n - m else "NO"

print(solve())
