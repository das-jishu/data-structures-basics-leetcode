""" 
# COMBINATION SUM II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30 
"""

def combinationSum2(candidates, target):
    candidates.sort()
    return combo(candidates, target)

def combo(candidates, target):

    if len(candidates) == 0 or target < min(candidates):
        return []

    result = []
    if target in candidates:
        result.append([target])

    for i, x in enumerate(candidates):
        if i > 0 and x == candidates[i - 1]:
            continue
        y = combo(candidates[i+1:], target - x)
        if len(y) == 0:
            continue
        for t in y:
            t.append(x)
            result.append(t)

    return result