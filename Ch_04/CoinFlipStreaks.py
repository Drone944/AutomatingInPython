import random
numberOfStreaks = 0
l1 = []
s = 0
for experimentNumber in range(10000):
	for i in range(100):
		l1.append(random.randint(0, 1))
	for j in range(len(l1)):
		if (j != (len(l1)-1)) and (l1[j] == l1[j+1]):
			s += 1
		else:
			s = 0
		if s == 5:
			numberOfStreaks += 1
			s = 0
	s = 0
	l1 = []
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))