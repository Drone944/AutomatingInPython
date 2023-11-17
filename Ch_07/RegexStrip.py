import re

def regstrip(s, c):
	lstrip = re.compile(r'^[' + re.escape(c) + r']*')
	rstrip = re.compile(r'[' + re.escape(c) + r']*$')
	s = re.sub(lstrip, '', s)   
	s = re.sub(rstrip, '', s)
	return s

s = input('Enter the string : ')
c = input('Enter the characters to be striped : ')
print(regstrip(s, c))