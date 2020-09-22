# coding = utf-8

def solve(letter: str, K: int) -> int:
    if not letter: return -1

    def rotate(s: int, K: int):
        if not s: return False

        n = len(s)
        if n == 1 or K == 0: return True

        for i in range(n):
            rotate_index = (i + K) % n
            if s[i] != s[rotate_index]: 
                return False

        return True

    res = 0
    
    word_list = letter.split(" ")
    for word in word_list:
        if rotate(word, K):
            res += 1
    
    return res