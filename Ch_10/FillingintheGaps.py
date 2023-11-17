import os, re, shutil

os.chdir(input('Enter the path of the directory : '))
p1 = input('Enter the prefix commmon to the filenames : ')
p = '(' + p1 + ')'

i = 1
regex = re.compile(p + r'(\d{,3})(.*)')
for f in os.listdir():
	mo = regex.search(f)
	if mo != None :
		st = '00' + str(i)
		s = mo.group(1) + st +mo.group(3)
		i += 1
		shutil.move(f, s)