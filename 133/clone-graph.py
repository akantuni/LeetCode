"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        memo = {}
        def dfs(node):
            if node is None:
                return
            if node in memo:
                return memo[node]

            copy = Node(node.val)
            memo[node] = copy
            for n in node.neighbors:
                memo[node].neighbors.append(dfs(n))

            return copy
        
        return dfs(node)
