"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""


class Solution():
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        """
        Method 1: Hash table - Beautiful Solution

        * Initially, enumerate through list1 - key:restaurant, value:[1, index]
        * Enumerate through list2:
        IF the value is in d, then it indicates the common restaurant
        we are interested in - key:restaurant, value:[2, sum(indexes)]
        * Filter out only those elements in the dict which have a value[0] == 2,
        implying that they occur in both the lists; this helps us find the
        minimum sum of one or more restaurants
        Note: We have to find the minimum sum earlier, since there can be 
        multiple restaurants

        Your runtime beats 61.37 % of python3 submissions.
        """
        d = {}

        for i, j in enumerate(list1):
            d[j] = [1, i]

        for i, j in enumerate(list2):
            if j in d:
                d[j][0] = 2
                d[j][1] += i

        min_sum = min([v[1] for k, v in d.items() if v[0] == 2])
        arr_restaurant = []

        for key, value in d.items():
            if value[0] == 2 and value[1] == min_sum:
                arr_restaurant.append(key)

        return arr_restaurant
