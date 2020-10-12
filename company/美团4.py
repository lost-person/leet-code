# coding = utf-8

class TreeNode:
    def __init__(self, index=None, color=None) -> None:
        self.index = index
        self.child_list = []
        self.color_list = []

def solve():
    n = int(input())
    
    # n个节点
    node_list = [TreeNode(index=i+1) for i in range(n)]
    for i in range(n - 1):
        par, child = map(int, input().split())
        node_list[par - 1].child_list.append(node_list[child - 1])

    # 每个节点的颜色
    color_list = list(map(int, input().split()))
    max_color = max(color_list)
    
    for i in range(n):
        node_list[i].color_list = [0] * max_color
        node_list[i].color_list[color_list[i] - 1] = 1

    
    def recur(node: TreeNode):
        if not len(node.child_list):
            return node
        
        for child in node.child_list:
            child_color_list = recur(child).color_list
            node.color_list = [color1 + color2 for color1, color2 in zip(node.color_list, child_color_list)]

        return node

    node_list[0] = recur(node_list[0])
    
    q = int(input())
    
    for i in range(q):
        node_index = int(input())
        color_list = node_list[node_index - 1].color_list
        max_color, max_color_index = -1, -1
        for i, color in enumerate(color_list):
            if max_color < color:
                max_color = color
                max_color_index = i
        print(max_color_index + 1)

solve()
