# coding = utf-8

def get_max(score_list):
    max_score, tmp = 0, 0
    
    for score in score_list:
        tmp += score
        if tmp < 0:
            tmp = 0
        max_score = max(max_score, tmp)
    
    return max_score

def get_min(score_list):
    min_score, tmp = 0, 0

    for score in score_list:
        tmp += score
        if tmp > 0:
            tmp = 0
        min_score = min(min_score, tmp)
    
    return min_score

def solve():
    T = int(input())

    while T > 0:
        T -= 1

        n = int(input())
        score_list = list(map(int, input().split()))

        max_score = get_max(score_list)
        min_score = get_min(score_list)

        sum_score = sum(score_list)

        return max(max_score, sum_score - min_score)


print(solve())
