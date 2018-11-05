"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        Method 1: Array - Brute Force

        * Iterate through all the Linked Lists and 
        store each value in a single array - O(n)
        * Sort the array - O(nlogn)
        * Create a Linked List
        """

        """
        Method 2: Heap

        * Create a heap with [node.val, index, node]
        lists = [[1,4,5],[1,3,4],[2,6]]
        heap = [(1,0,<l1>), (1,1,<l2>), (2,2,<l3>)]
        Since we want the key of the heap to be based on 
        the value of the element, we should put that first in the tuple.

        * Pop the minimum element from the heap,
        this is done by heapq.heappop(heap)

        * Add the next tuple into the heap
        """

        heap = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapq.heapify(heap)

        # #Initialize head and tail
        head, tail = None, None
        while heap:
            # #Pop the minimum element from the heap
            node_val, index, node = heapq.heappop(heap)

            # #Add the next tuple into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

            if not head:
                head, tail = node, node
            else:
                tail.next = node
                tail = node

        return head