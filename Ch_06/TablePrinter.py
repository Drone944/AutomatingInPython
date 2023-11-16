def printTable(tableData):
	colWidths = [0] * len(tableData)
	for j in range(3):
		c = 0
		for i in range(len(tableData[j])):
			if len(tableData[j][i]) > c:
				c = len(tableData[j][i])
		colWidths[j] = c
	for i in range(len(tableData[0])):
		for j in range(3):
			print(tableData[j][i].rjust(colWidths[j] + 1), end = '')
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

