"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Your runtime beats 55.23 % of python submissions.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # #Method 1:
        def sum_sq_digits(n):
            res = 0
            while n:
                res += (n%10)**2
                n = n//10
            return res


        bool = True
        s = set()
        while bool:
            ssd_res = sum_sq_digits(n)

            if ssd_res == 1:
                return True
            else:
                if ssd_res in s:
                    return False
                else:
                    print(ssd_res)
                    s.add(ssd_res)
                    n = ssd_res

        # #Method 2
        bool = True
        s = set()
        f = lambda x:int(x)**2

        while bool:
            ssd_res = sum(list(map(f, list(str(n)))))

            if ssd_res == 1:
                return True
            elif ssd_res in s:
                    return False
            else:
                s.add(ssd_res)
                n = ssd_res

        # # #Method 3
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

        # # #Method 4
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            # #It is interesting that the number will always
            # #contain 4.
            if n == 4:
                return False
        else:
            return True
