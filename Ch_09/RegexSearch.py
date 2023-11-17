import re, os, glob

d = input('Enter the path of the directory : ')
os.chdir(d)
regex = re.compile(input('Enter your regex expression :'))
for ftxt in glob.glob('*.txt'):
	f = open(ftxt)
	s = f.read()
	mo = regex.search(s)
	if mo == None:
		print('Not found.')
	else:
		o = mo.group()
		print('Found :')
		print(o)

