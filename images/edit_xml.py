# 
import glob
	
import xml.etree.ElementTree as ET


for filename in glob.glob('*.xml'):
	
	
	
	
	tree = ET.parse(filename)
	root = tree.getroot()
	root[4][0].text = '2448'
	root[4][1].text = '2048'
	
	
	tree.write(filename)
	
