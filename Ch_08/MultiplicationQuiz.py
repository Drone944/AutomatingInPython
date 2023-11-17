import pyinputplus as pyip
import random 

c = 0
for i in range(10):
	a = random.randint(0, 9)
	b = random.randint(0, 9)
	s = str(a) + ' x ' + str(b) +' = '
	try:
		product = pyip.inputInt(s, allowRegexes=['^%s$' % (a * b)], blockRegexes=[('.*', 'Incorrect!')], limit = 3, timeout = 8)
		if product == a * b:
			print('Correct !')
			c += 1
	except pyip.TimeoutException:
		print('Out of time!')
	except pyip.RetryLimitException:
		print('Out of tries!')
print('The score = ', c)
