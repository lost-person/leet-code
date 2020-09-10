
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # visited = dict()
        # def copy_randomList(node):
        #     if not node:
        #         return node

        #     if node in visited:
        #         return visited[node]
            
        #     clone = Node(node.val)
        #     visited[node] = clone
        #     clone.next = copy_randomList(node.next)
        #     clone.random = copy_randomList(node.random)
        #     return clone
        
        # return copy_randomList(head)

        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        
        p = head
        while p:
            next_origin = p.next.next
            p.next.next = next_origin.next if next_origin else None
            p.next.random = p.random.next if p.random else None
            p = next_origin
        
        return head.next
