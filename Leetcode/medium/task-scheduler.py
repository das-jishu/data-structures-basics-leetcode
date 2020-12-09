""" 
# TASK SCHEDULER

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 
Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100]. 
"""

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        # Note the frequency of every character
        freq = [0] * 26
        
        for char in tasks:
            freq[ord(char) - ord('A')] += 1
        
        # Sort the frequency
        freq.sort()
        
        # Get maximum frequency
        # This will be used for calculation of idle time
        max_freq = freq.pop()
        
        # Initial idle time (without going through all other tasks)
        idle_time = (max_freq - 1) * n
        
        # Now we go through other tasks and see how we can adjust the idle time
        while freq and idle_time > 0:
            idle_time -= min(max_freq - 1, freq.pop())
        
        idle_time = max(0, idle_time)
        
        return idle_time + len(tasks)