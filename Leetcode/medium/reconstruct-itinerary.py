"""
# RECONSTRUCT ITINERARY

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
from.length == 3
to.length == 3
from and to consist of uppercase English letters.
from != to
"""

class Solution:
    def findItinerary(self, tickets):
        neighborsList = {}
        remainingPlaces = {}
        
        for ticket in tickets:
            start, end = ticket
            string = self.convert(start, end)            
            if start not in neighborsList:
                neighborsList[start] = []
            neighborsList[start].append(end)
            if string not in remainingPlaces:
                remainingPlaces[string] = 0
            remainingPlaces[string] += 1
        
        for edges in neighborsList:
            neighborsList[edges].sort()
            
        return self.dfs("JFK", neighborsList, ["JFK"], len(tickets), remainingPlaces)
    
    def dfs(self, current, neighbors, itinerary, n, remainingPlaces):
        if len(itinerary) == n + 1:
            return itinerary
        
        if current not in neighbors:
            return False
        
        for destination in neighbors[current]:
            journey = self.convert(current, destination)
            if journey not in remainingPlaces or remainingPlaces[journey] == 0:
                continue
            remainingPlaces[journey] -= 1
            itinerary.append(destination)
            check = self.dfs(destination, neighbors, itinerary, n, remainingPlaces)
            if check != False:
                return check
            remainingPlaces[journey] += 1
            itinerary.pop()
        return False
            
    def convert(self, a, b):
        return str(a) + "-" + str(b)
            
                
        
        
            