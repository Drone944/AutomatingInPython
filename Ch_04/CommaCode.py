def commacode(l1):
	s1 = ''
	for i in range(len(l1)):
		if i == (len(l1)-1):
			s1 = s1 + 'and ' +l1[i]
		else:
			s1 = s1 + l1[i] + ', '
	print(s1)
li = eval(input("Enter a list : "))
commacode(li)