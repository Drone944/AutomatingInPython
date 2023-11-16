f = open('replace.txt', 'r')

l1 = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
rf = f.readlines()
for i in rf:
	s = i.split()
	indexi = rf.index(i)
	for j in s:
		if j.startswith('ADJECTIVE') or j.startswith('NOUN') or j.startswith('ADVERB') or j.startswith('VERB'):
			if j[0] == 'A':
				print('Enter an', j,': ')
				word = input()
			else:
				print('Enter a', j,': ')
				word = input()
			indexj = s.index(j)
			s[indexj] = word
	rf[indexi] = s

q = ''
for i in range(len(rf)):
	for j in range(len(rf[i])):
		q = q + rf[i][j] + ' '

f.close()

f = open('new.txt', 'w+')

f.write(str(q))
f.flush()
f.seek(0)
print(f.read())

f.close()

