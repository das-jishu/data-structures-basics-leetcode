""" 
# SUM OF DISTANCES IN TREE

An undirected, connected tree with n nodes labelled 0...n-1 and n-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= n <= 10000 
"""

class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        graph = [[] for i in range(n)]
        for edge in edges:
            start, end = edge
            graph[start].append(end)
            graph[end].append(start)
            
        count = [1 for i in range(n)]
        distance = [0 for i in range(n)]
        self.dfs(graph, 0, None, count, distance)
        self.fillUpRest(graph, 0, None, count, distance)
        return distance        
        
    def dfs(self, graph, current, parent, count, distance):
        for child in graph[current]:
            if child == parent:
                continue
            self.dfs(graph, child, current, count, distance)
            count[current] += count[child]
            distance[current] += distance[child] + count[child]
        return
    
    def fillUpRest(self, graph, current, parent, count, distance):
        for child in graph[current]:
            if child == parent:
                continue
            distance[child] = distance[current] - count[child] + len(graph) - count[child]
            self.fillUpRest(graph, child, current, count, distance)
        return