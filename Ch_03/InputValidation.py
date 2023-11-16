def collatz(number):
	if number % 2 == 0:
		c = number // 2
	else:
		c = 3 * number + 1
	return c

try:
	n = int(input("Enter number : "))
	f = 0
	while(f != 1):
		f = collatz(n)
		n = f
		print(f)
except:
	print('Enter a valid integer.')