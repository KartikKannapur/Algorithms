# Uses python3
__author__ = "Kartik Kannapur"

# #Import Libraries
import sys

# #Algorithm:
# #Essentially we need to pick the 2 largest elements from the array
# #Method 1: Sort the array and select the two largest elements - Very expensive
# #Method 2: Scan the entire array twice by maintaining two indexes - Max1 and Max 2 - 
# #Can this be reduced to one operation?

# #Method 3: Scan the array once, keeping a track of the largest element and the second largest
# #while looping through the array itself.

arr_len = int(sys.stdin.readline())
arr_vals = sys.stdin.readline()
arr = [int(elem) for elem in arr_vals.split()]

max_one = arr[0]
max_two = arr[0]

# #Linear Search 
if len(arr) == 2:
	max_one = arr[0]
	max_two = arr[1]

if len(arr) > 2:	
	for element in arr:
		if element >= max_one:
			max_two = max_one
			max_one = element

		if (element > max_two) and (element < max_one):
			max_two = element



# print(max_one, max_two, "Product:", (max_one*max_two))
print((max_one*max_two))
