import package1.mod1 
import package1.mod1 as pack1

print package1.mod1.string
print pack1.string

print package1.global_var #global_var from __init__.py in package1

print dir(package1)

#check behaviours of all of below
from package1 import *
#from package1.package2 import *
print dir(pack1)