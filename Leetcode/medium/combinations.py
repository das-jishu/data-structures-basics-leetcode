""" 
# COMBINATIONS

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
 
Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

Constraints:

1 <= n <= 20
1 <= k <= n 
"""

def combine(n: int, k: int):
    return combo(1, k, n)
    
def combo(start, k, n):
    if k > n - start + 1:
        return []
    
    result = []
    if k == 1:
        for i in range(start, n+1):
            result.append([i])

    else:
        for x in range(start, n):
            t = combo(x + 1, k - 1, n)
            if len(t) == 0:
                continue
            for temp in t:
                temp.insert(0, x)
                result.append(temp)
            
    return result