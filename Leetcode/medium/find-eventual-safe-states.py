""" 
# FIND EVENTUAL SAFE STATES

We start at some node in a directed graph, and every turn, we walk along a directed edge of the graph. If we reach a terminal node (that is, it has no outgoing directed edges), we stop.

We define a starting node to be safe if we must eventually walk to a terminal node. More specifically, there is a natural number k, so that we must have stopped at a terminal node in less than k steps for any choice of where to walk.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

The directed graph has n nodes with labels from 0 to n - 1, where n is the length of graph. The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph, going from node i to node j.

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.

Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].legnth <= n
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104]. 
"""

class Solution:
    def eventualSafeNodes(self, graph):
        safeNodes = []
        safe = {}
        for vertex in range(len(graph)):
            if vertex not in safe:
                self.checkForSafety(graph, vertex, safe)
                
        safeNodes = [node for node in safe if safe[node] == True]
        return sorted(safeNodes)
    
    def checkForSafety(self, graph, current, safe):
        if current in safe:
            return safe[current]
        
        if current not in safe:
            safe[current] = False
        
        isCurrentSafe = True
        for neighbor in graph[current]:
            safety = self.checkForSafety(graph, neighbor, safe)
            if not safety:
                isCurrentSafe = False
                
        safe[current] = isCurrentSafe
        return safe[current]

## TIME LIMIT EXCEEDED ##

"""class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNodes = []
        for vertex in range(len(graph)):
            if not self.checkForCycles(graph, vertex, set()):
                safeNodes.append(vertex)
                
        return safeNodes
    
    def checkForCycles(self, graph, current, visited):
        #print("current:",current,"visited:",visited)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor in visited:
                return True
            check = self.checkForCycles(graph, neighbor, visited)
            if check:
                return check
        visited.remove(current)
        return False"""
    