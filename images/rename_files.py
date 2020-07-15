import glob
import os
count = 0
for filename in glob.glob('*.png'):
	start = 'sharp_'
	count = count +1
	num = str(count)
	end = '.jpg'
	new_name = start + num + end
	os.rename(filename, new_name)
	 
	
	
	
	
