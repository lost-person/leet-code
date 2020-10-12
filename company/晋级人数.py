# coding = utf-8

def solve():
    n, x = map(int, input().split())
    score_list = list(map(int, input().split()))

    score_list = list(sorted(score_list, key=lambda x: -x))
    limit_score = score_list[x - 1]

    res = 0
    for score in score_list:
        if score == 0 or score < limit_score:
            break
        
        res += 1
    
    return res

print(solve())
