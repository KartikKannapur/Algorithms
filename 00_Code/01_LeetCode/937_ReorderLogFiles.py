"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        """
        Method: Sort + Questions Logic

        * Segreate the logs based on the word after
        the identifier, into digit and letter logs
        * Interesting sorted() function - sorting based
        on 2 parameters
        sorted(arr, key=lambda x:(x[1], x[0]))

        61 / 61 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        """

        arr_digit_logs = []
        arr_letter_logs = []

        for ele in logs:
            if ele.split()[1].isnumeric():
                arr_digit_logs.append(ele)
            else:
                arr_letter_logs.append(ele)

        return (sorted(arr_letter_logs, key=lambda ele: (ele.split()[1:], ele.split()[0])) + arr_digit_logs)