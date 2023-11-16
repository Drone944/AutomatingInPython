import os
import shutil

for foldername, subfolders, filenames in os.walk('/home/ironman/trial1'):
	for i in filenames:
		if i.endswith('.pdf') or i.endswith('.jpg'):
			di = foldername + '/' + i
shutil.copy(di, '/home/ironman/trial2')
