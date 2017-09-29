__author__ = "Kartik Kannapur"

# #Recursive Function - Factorial

def fact(num):
	if num >= 0:
		if num == 0:
			return 1
		else:
			return num*fact(num-1)

	else:
		return -1

def test_cases():
	assert fact(4) == 24, "Factorial of 4 is incorrect"
	assert fact(1) == 1, "Factorial of 1 is incorrect"
	assert fact(0) == 1, "Factorial of 0 is incorrect"
	assert fact(-5) == -1, "Factorial of negative numbers does not exist"

	print("---Test Cases: Pass---")

test_cases()