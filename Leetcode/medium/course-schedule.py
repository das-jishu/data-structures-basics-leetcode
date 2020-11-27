""" 
# COURSE SCHEDULE

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5 
"""

class Solution:
    def __init__(self):
        self.flag = True
    
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        
        d = {}
        for x in prerequisites:
            if x[0] not in d:
                d[x[0]] = [x[1]]
            else:
                d[x[0]].append(x[1])
        
        perm = set()  
        for x in range(numCourses):
            temp = set()
            self.check(x, perm, temp, d)
            if not self.flag:
                return False
            
        return True
        
    def check(self, n, perm, temp, d):
        if n in perm:
            return
        
        if n in temp:
            self.flag = False
            return
        
        temp.add(n)
        if n in d:
            for m in d[n]:
                self.check(m, perm, temp, d)
            
        temp.remove(n)
        perm.add(n)