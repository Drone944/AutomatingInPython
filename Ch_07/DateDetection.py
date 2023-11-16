import re

date = input('Enter a date : ')
regexobj = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo = regexobj.search(date)
day = int(mo.group(1))
month = int(mo.group(2))
year = int(mo.group(3))
l31 = [1,3,5,7,8,10,12]
l30 = [4,6,9,11]
flag = 0

if month <= 12 and month >= 1:
	if month in l30:
		if day <= 30 and day >=1:
			flag = 1
		else:
			flag = 0
	elif month in l31:
		if day <= 31 and day >=1:
			flag = 1
		else:
			flag = 0
	elif month == 2:
		if year%4 == 0 and (year%100 == 0 and year%400 == 0):
			if day <= 29 and day >=1:
				flag = 1
			else:
				flag = 0
		else:
			if day <= 28 and day >=1:
				flag = 1
			else:
				flag = 0
	else:
		flag = 0
else:
	flag = 0

if flag == 1:
	print('It is a valid date.')
else:
	print('It is not a valid date')





