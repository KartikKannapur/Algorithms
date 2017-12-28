words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]


arr = []

for word in words:
	var_counter = 0
	for counter in range(len(word)):
		if word[:counter] in words:
			# print(word, word[:counter])
			var_counter += 1

		if len(word) == var_counter+1:
			# print(word)
			arr.append(word)


l = len(sorted(arr)[-1])

arr2 = []
for ele in arr:
	if len(ele) == l:
		arr2.append(ele)

return(sorted(arr2)[0])


	# if all(True if word[:counter] in words else False for counter in range(len(word)+1)) == True:
	# 	print(word)