__author__ = "Kartik Kannapur"

# #Greatest Common Divisor

def gcd_naive(a, b):

	if a == 0:
		return b

	if b == 0:
		return a

	var_largest = 1
	for val in range(1, max(a,b)+1):
		# print(val)
		if (a%val == 0) and (b%val == 0):
			# print(a, b, val)
			var_largest = val

	return var_largest

def gcd_efficient(a, b):
	if a == 0:
		return b

	if b == 0:
		return a

	if a > b:
		return gcd_efficient(b, a%b)
	else:
		return gcd_efficient(a, b%a)


# print(gcd_naive(10, 5))
print(gcd_efficient(3918848, 1653264)) #61232
print(gcd_efficient(357, 243)) #3
