"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only
push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You
may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or
peek operations will be called on an empty queue).

Your runtime beats 56.80 % of python submissions.
"""


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        self.stack_in.append(x)

        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack_in.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack_in[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.stack_in) and (not self.stack_out)




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()