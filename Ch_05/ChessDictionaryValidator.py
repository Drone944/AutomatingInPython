def isValidChessBoard(dict1):
	t = 0
	y = 0
	l1 = ['1','2','3','4','5','6','7','8']
	l2 = ['a','b','c','d','e','f','g','h']
	keys = list(dict1.keys())
	values = list(dict1.values())
	real = {'wking':1, 'wqueen':1, 'wpawn':8, 'wbishop':2, 'wknight':2, 'wrook':2, 'bking':1, 'bqueen':1, 'bpawn':8, 'bbishop':2, 'bknight':2, 'brook':2,}
	if (len(keys) <= 32) and ((values.count('wking') == 1) and (values.count('bking') == 1)):
		for i in keys:
			if (i[0] in l1) and (i[1] in l2):
				t = 1
			else:
				t = 0
				break
		for j in values:
			if (j in values) and (values.count(j) <= real[j]):
				y = 1
			else:
				y = 0
				break
	if t == 1 and y == 1:
	    return True
	else:
	    return False
d1 = eval(input("Enter a chess board dictionary : "))
T = isValidChessBoard(d1)
print(T)