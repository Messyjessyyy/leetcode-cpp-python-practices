#Clone graph 

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            
            copy = Node(n.val)
            old_to_new[n] = copy
            
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)

# #BFS approach
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return None
#         old_to_new = {node: Node(node.val)}
#         queue = [node]
# 
