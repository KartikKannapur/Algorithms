__author__ = "Kartik Kannapur"

# #Fibonacci Numbers - Recursive Function

def fib_naive(n):
	if n <= 1:
		return n
	else:
		return fib_naive(n-1) + fib_naive(n-2)



def fib_efficient(n):
	arr_fib = [0, 1]

	for elem in range(2, n+1):
		arr_fib.append(arr_fib[elem-1] + arr_fib[elem-2])

	return arr_fib[-1]

number = 5

print(fib_naive(number))

print(fib_efficient(number))
