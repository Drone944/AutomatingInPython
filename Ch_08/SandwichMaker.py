import pyinputplus as pyip

p = 0
bdict = {'Wheat' : 15, 'White' : 20, 'Sourdough' : 25}
pdict = {'Chicken' : 10, 'Turkey' : 15, 'Ham' : 20, 'Tofu' : 25}
cdict = {'Cheddar' : 15, 'Swiss' : 20, 'Mozzarella' : 25}
kdict = {'Mayo' : 5, 'Mustard' : 10, 'lettuce' : 15, 'tomato' : 15}

btype = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt = 'What bread type would you like ? : \n')
p += bdict[btype]
ptype = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt = 'What protein type would you like ? : \n')
p += pdict[ptype]
c = pyip.inputYesNo('Do you want cheese ? : ')
if c == 'yes':
	ctype = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt = 'What cheese type would you like ? : \n')
	p += cdict[ctype]
k = pyip.inputYesNo('Do you want mayo, mustard, lettuce, or tomato ? (Enter yes or no) : ')
if k == 'yes':
	ktype = pyip.inputMenu(['Mayo', 'Mustard', 'lettuce', 'tomato'], prompt = 'What would you like ? : \n')
	p += kdict[ktype]
n = pyip.inputInt('How many sandwhiches do you want : ', min = 1)
p *= n

print('The price is : ', p)
