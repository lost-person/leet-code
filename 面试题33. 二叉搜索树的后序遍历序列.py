class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        
        n = len(postorder)
        
        # def recur(low, high):
        #     if low >= high:
        #         return True
            
        #     i = low
        #     while postorder[i] < postorder[high]:
        #         i += 1
            
        #     mid = i
        #     while postorder[i] > postorder[high]:
        #         i += 1
            
        #     return i == high and recur(low, mid - 1) and recur(mid, high - 1)
        
        # return recur(0, n - 1)

        stack, root = [], float('inf')
        for i in range(n - 1, -1, -1):
            if postorder[i] > root:
                return False
            
            while stack and stack[-1] > postorder[i]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
