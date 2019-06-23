"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Method 1: Array
        * Create an array with all zeros to start with
        * For each of the trips in the `trips` array, add
        the number of passengers between the start and end index
        
        [[2,1,5],[3,3,7]]
        arr = [0 0 0 0 0 0 0]
        arr = [2 2 2 2 2 0 0]
        arr = [2 2 5 5 5 3 3]
        
        Check if the largest number in the arr is greater than
        the seat capacity
        
        53 / 53 test cases passed.
        Status: Accepted
        Runtime: 184 ms
        Memory Usage: 13.4 MB
        """
        
        max_len = max(ele[2] for ele in trips)
        arr = [0]*max_len
        
        # #Load values into `arr`
        for ele in trips:
            for index in range(ele[1], ele[2]):
                arr[index] += ele[0]
                
        if  max(arr)> capacity:
            return False
        return True
