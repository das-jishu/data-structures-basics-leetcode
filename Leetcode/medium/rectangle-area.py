""" 
# RECTANGLE AREA

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45 
"""

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        areaA = (C - A) * (D - B)
        areaB = (G - E) * (H - F)
        common = 0
        
        if C <= E or A >= G:
            common = 0
        
        elif B >= H or D <= F:
            common = 0
            
        else:
            x = [A, C, E, G]
            y = [B, F, D, H]
            x.sort()
            y.sort()
            common = (x[2] - x[1]) * (y[2] - y[1])
            
        return areaA + areaB - common