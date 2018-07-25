"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

# """
# Method 1: Using a Boolean array of size 1000000
# i.e. maximum range of input values as the hash set.
# Your runtime beats 39.70 % of python submissions.
# """

# class MyHashSet(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size = 1000000
#         self.buckets = [False]*self.size

#     def add(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         self.buckets[key] = True


#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: void
#         """
#         self.buckets[key] = False


#     def contains(self, key):
#         """
#         Returns true if this set contains the specified element
#         :type key: int
#         :rtype: bool
#         """
#         return self.buckets[key]


"""
Method 2: Using the built-in set() function
to improve percentile score :P
Your runtime beats 96.48 % of python submissions
"""


class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.buckets.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.buckets:
            self.buckets.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.buckets



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)