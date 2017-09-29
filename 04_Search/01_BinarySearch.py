__author__ = "Kartik Kannapur"

# #Binary Search

def binarySearch(arr_input, min_val, max_val, target):
	# #Check if the length of the array is greater than 0
	if len(arr_input) > 0:

		if min_val > max_val:
			return -1

		mid_val = (min_val + max_val)//2
		# print(mid_val)

		if target == arr_input[mid_val]:
			print("Element found: ", target, " at the index: ", mid_val)
			return mid_val

		elif target < arr_input[mid_val]:
			# print(arr_input[min_val:mid_val])
			binarySearch(arr_input, min_val, mid_val-1, target)

		else:
			# print(arr_input[mid_val+1:max_val+1])
			binarySearch(arr_input, mid_val+1, max_val, target)

	else:
		return -1


binarySearch([1,2,4,5,6,10,11], 0, 6, 10)
binarySearch([1,2,4,5,10,11], 0, 5, 10)
binarySearch([1,2,4,5,6,10,11,18,21,33,45,67], 0, 11, 67)