import os

print dir(os) #prints all the methods available in os module

print os.getenv('os')

print os.listdir(os.getcwd())

path = r"E:\Programs\Python\SublimeText\Class11_[25-11-2018]"
#os.mkdir(path+r'\test_path')

print os.listdir(path+r'\test_path')

import os.path
import sys

print sys.modules
print sys.modules.keys()
print sys.modules['os'] #platform specific file

print os.path.isdir(path)

for a,b,c in os.walk("path",topdown=false):
	print "a=%s" %(a)