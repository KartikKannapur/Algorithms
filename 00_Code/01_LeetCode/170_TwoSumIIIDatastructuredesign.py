"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5); find(4) -> true find(7) -> false

Hints:
Don't forget there may be duplicate elements in this question.
For example,
add(2), add(2), find(4) -> True

So, we need a hash table instead of hash set.
When we traverse each key in the hash table to find the sum:
If key * 2 = sum: its value should be >= 2
If key * 2 ! = sum: (sum - key) should be in the table.
"""


class TwoSum:
    def __init__(self):
        self.d = {}

    def add(self, number):
        if number in self.d:
            self.d[number] += 1
        else:
            self.d[number] = 1

    def find(self, value):
        for key in self.d:
            if key * 2 == value:
                if self.d[key] >= 2:
                    return True
            elif value - key in self.d:
                return True

        return False