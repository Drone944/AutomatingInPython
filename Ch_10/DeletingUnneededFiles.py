import os

for foldername, subfolders, filenames in os.walk('/home/ironman/trial1'):
	for i in filenames:
		if os.path.getsize(foldername + '/' + i) > 1048576:
			print(foldername + '/' + i)
