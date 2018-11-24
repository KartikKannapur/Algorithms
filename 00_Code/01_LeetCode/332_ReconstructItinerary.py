"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        """
        Reference: Discussion Forum
        """
        d = {}
        for ticket in tickets:
            if ticket[0] not in d:
                d[ticket[0]] = [ticket[1]]
            else:
                d[ticket[0]].append(ticket[1])

        for ticket in d:
            d[ticket].sort()

        res = ['JFK']
        end = []
        while d:
            if res[-1] not in d:
                end.append(res[-1])
                res.pop()
                continue
            fr, to = res[-1], d[res[-1]].pop(0)
            res.append(to)
            if len(d[fr]) == 0:
                d.pop(fr)

        if end:
            res += end[::-1]

        return res