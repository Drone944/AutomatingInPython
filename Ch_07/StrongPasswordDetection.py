import re

s = input('Enter the password : ')
if len(s) >= 8:
	regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])')
	mo = regex.search(s)
	if mo == None:
		print('The password is not strong.')
	else:
		print('The password is strong.')
else:
	print('The password is not strong.')
